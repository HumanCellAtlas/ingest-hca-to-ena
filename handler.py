import json
import os
import argparse
import uuid
import base64
import xml.etree.ElementTree as ET
from xml.dom import minidom
import zipfile
import re


def zipdir(job_id):
    # path = "/tmp/" + job_id
    path = "examples/tmp/" + job_id
    zip_file_path = path + '.zip'
    zf = zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED)
    for file in os.listdir(path):
        zf.write(path + "/" + file, file)
    zf.close()
    return zip_file_path


def handle_convert(event, context):
    submitted_json = _process_event(event)
    print(submitted_json)
    job_id = str(uuid.uuid1())
    print("Starting job: " + job_id)
    convert(submitted_json, job_id)
    zip_file_path = zipdir(job_id)
    print("Finished job: " + job_id)
    with open(zip_file_path, "rb") as zip_file:
        encoded_string = base64.b64encode(zip_file.read())
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/zip",
            "Content-Disposition": "attachment; filename=" + job_id + ".zip"
        },
        "body": str(encoded_string.decode("utf-8")),
        "isBase64Encoded": True
    }
    return response


_study_ref = None


def _add_run_xml(run_set_element, file_json):
    if file_json['read_index'] in ('read1'): # read1 is the only required read/file for each run
        run_element = ET.SubElement(run_set_element, 'RUN')
        # TODO: determine how to link to experiment ref
        experiment_ref_element = ET.SubElement(run_element, 'EXPERIMENT_REF')
        data_block_element = ET.SubElement(run_element, 'DATA_BLOCK')
        files_element = ET.SubElement(data_block_element, 'FILES')
        file_element = ET.SubElement(files_element, 'FILE')
        file_element.set('filetype', 'bam')
        file_element.set('checksum_method', 'MD5')
        # TODO: create md5 checksum for files
        file_element.set('checksum', '')
        if 'file_core' in file_json:
            file_core = file_json['file_core']
            if 'file_name' in file_core:
                # TODO: convert fastq|fastq.gz to bam
                print(file_core['file_name'])
                bam_file_name = re.sub("_R1","",file_core['file_name'].split('fastq')[0]) + 'bam'
                print(bam_file_name)
                run_element.set('alias', bam_file_name)
                file_element.set('filename', bam_file_name)


def _add_experiment_xml(experiment_set_element, process_json):
    experiment_element = ET.SubElement(experiment_set_element, 'EXPERIMENT')
    title_element = ET.SubElement(experiment_element, 'TITLE')
    study_ref_element = ET.SubElement(experiment_element, 'STUDY_REF')
    design_element = ET.SubElement(experiment_element, 'DESIGN')
    design_description_element = ET.SubElement(design_element, 'DESIGN_DESCRIPTION')
    # TODO: determine and add sample refname
    sample_descriptor_element = ET.SubElement(design_element, 'SAMPLE_DESCRIPTOR')
    library_descriptor_element = ET.SubElement(design_element, 'LIBRARY_DESCRIPTOR')
    library_strategy_element = ET.SubElement(library_descriptor_element, 'LIBRARY_STRATEGY')
    library_source_element = ET.SubElement(library_descriptor_element, 'LIBRARY_SOURCE')
    library_selection_element = ET.SubElement(library_descriptor_element, 'LIBRARY_SELECTION')
    library_layout_element = ET.SubElement(library_descriptor_element, 'LIBRARY_LAYOUT')
    single_element = ET.SubElement(library_layout_element, 'SINGLE')
    platform_element = ET.SubElement(experiment_element, 'PLATFORM')
    illumina_element = ET.SubElement(platform_element, 'ILLUMINA')
    instrument_model_element = ET.SubElement(illumina_element, 'INSTRUMENT_MODEL')
    # TODO: check library strategy value
    library_strategy_element.text = "RNA-Seq"
    library_source_element.text = "TRANSCRIPTOMIC SINGLE CELL"
    # TODO: check library selection value
    # library_selection_element.text = "unspecified"
    library_selection_element.text = "TODO"
    instrument_model_element.text = "unspecified"
    if 'process_core' in process_json:
        process_core = process_json['process_core']
        if 'process_id' in process_core:
            experiment_element.set('alias', process_core['process_id'])
        if 'process_name' in process_core:
            title_element.text = process_core['process_name']
        if _study_ref:
            study_ref_element.set('refname', _study_ref)


def _add_sample_xml(sample_set_element, biomaterial_json):
    sample_element = ET.SubElement(sample_set_element, 'SAMPLE')
    title_element = ET.SubElement(sample_element, 'TITLE')
    sample_name_element = ET.SubElement(sample_element, 'SAMPLE_NAME')
    # sample_attributes_elements = ET.SubElement(sample_element, 'SAMPLE ATTRIBUTES')
    taxon_id_element = ET.SubElement(sample_name_element, 'TAXON_ID')
    if 'biomaterial_core' in biomaterial_json:
        biomaterial_core = biomaterial_json['biomaterial_core']
        if 'biomaterial_id' in biomaterial_core:
            sample_element.set('alias', biomaterial_core['biomaterial_id'])
        if 'biomaterial_name' in biomaterial_core:
            title_element.text = biomaterial_core['biomaterial_name']
        if 'ncbi_taxon_id' in biomaterial_core:
            taxon_id_element.text = str(biomaterial_core['ncbi_taxon_id'][0])

def _add_project_xml(project_set_element, project_json):
    project_element = ET.SubElement(project_set_element, 'PROJECT')
    name_element = ET.SubElement(project_element, 'NAME')
    title_element = ET.SubElement(project_element, 'TITLE')
    description_element = ET.SubElement(project_element, 'DESCRIPTION')
    submission_project_element = ET.SubElement(project_element, 'SUBMISSION_PROJECT')
    ET.SubElement(submission_project_element, 'SEQUENCING_PROJECT')
    if 'project_core' in project_json:
        project_core = project_json['project_core']
        if 'project_shortname' in project_core:
            shortname = project_core['project_shortname']
            project_element.set('alias', shortname)
            name_element.text = shortname
            global _study_ref
            _study_ref = shortname
        if 'project_title' in project_core:
            title_element.text = project_core['project_title']
        if 'project_description' in project_core:
            description_element.text = project_core['project_description']


def _create_project_set_xml(projects_json):
    project_set_element = ET.Element('PROJECT_SET')
    for project_json in projects_json:
        _add_project_xml(project_set_element, project_json)
    project_set_xml = ET.tostring(project_set_element)
    return project_set_xml


def _create_sample_set_xml(biomaterials_json):
    sample_set_element = ET.Element('SAMPLE_SET')
    for biomaterial_json in biomaterials_json:
        _add_sample_xml(sample_set_element, biomaterial_json)
    sample_set_xml = ET.tostring(sample_set_element)
    return sample_set_xml


def _create_experiment_set_xml(processes_json):
    experiment_set_element = ET.Element('EXPERIMENT_SET')
    for process_json in processes_json:
        _add_experiment_xml(experiment_set_element, process_json)
    experiment_set_xml = ET.tostring(experiment_set_element)
    return experiment_set_xml


def _create_run_set_xml(files_json):
    run_set_element = ET.Element('RUN_SET')
    for file_json in files_json:
        _add_run_xml(run_set_element, file_json)
    run_set_xml = ET.tostring(run_set_element)
    return run_set_xml


def _create_submission_xml():
    submission_element = ET.Element('SUBMISSION')
    actions_element = ET.SubElement(submission_element, 'ACTIONS')
    action_element = ET.SubElement(actions_element, 'ACTION')
    ET.SubElement(action_element, 'ADD')
    submission_xml = ET.tostring(submission_element)
    return submission_xml


def convert(dataset_json, job_id):
    submission_xml = _create_submission_xml()
    _output_xml("submission", submission_xml, job_id)
    for element in dataset_json:
        if 'schema_type' in element:
            schema_type = element['schema_type']
            if schema_type == 'project':
                if 'content' in element:
                    project_set_xml = _create_project_set_xml(element['content'])
                    _output_xml("project", project_set_xml, job_id)
            if schema_type == 'biomaterial':
                if 'content' in element:
                    sample_set_xml = _create_sample_set_xml(element['content'])
                    _output_xml("sample", sample_set_xml, job_id)
            if schema_type == 'process':
                if 'content' in element:
                    experiment_set_xml = _create_experiment_set_xml(element['content'])
                    _output_xml("experiment", experiment_set_xml, job_id)
            if schema_type == 'file':
                if 'content' in element:
                    run_set_xml = _create_run_set_xml(element['content'])
                    _output_xml("run", run_set_xml, job_id)


def _process_event(event):
    submitted_json = json.loads(event["body"])
    return submitted_json


def _output_xml(xml_type, xml_string, job_id):
    # output_dir = "/tmp/" + job_id
    output_dir = "examples/tmp/" + job_id
    try:
        os.stat(output_dir)
    except:
        os.mkdir(output_dir)
    xml_str = minidom.parseString(xml_string).toprettyxml(indent="   ")
    with open(output_dir + "/" + xml_type + ".xml", "w") as f:
        f.write(xml_str)


def main(file_path):
    with open(file_path) as json_data:
        job_id = str(uuid.uuid1())
        dataset_json = json.load(json_data)
        print("Starting job: " + job_id)
        convert(dataset_json, job_id)
        zip_file_path = zipdir(job_id)
        print("Finished job: " + job_id)
        print("Results in: " + zip_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Converts HCA JSON to ENA XML.')
    parser.add_argument("source", type=str, help='Source JSON')
    args = parser.parse_args()
    main(args.source)
