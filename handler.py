import json
import xml.etree.ElementTree as ET
from xml.dom import minidom


def handle(event, context):
    submission = _process_event(event)
    response = {
        "statusCode": 200,
        "body": {}
    }
    return response


# <EXPERIMENT_SET>
#    <EXPERIMENT alias="TODO: process_id (if this is unique for a given BAM)">
#        <TITLE>TODO: do not provide (is optional) or possibly process_name</TITLE>
#        <STUDY_REF refname="TODO: study alias"/>
#        <DESIGN>
#            <DESIGN_DESCRIPTION/>
#            <SAMPLE_DESCRIPTOR  refname="TODO: sample alias"/>
#            <LIBRARY_DESCRIPTOR>
#                <LIBRARY_STRATEGY>TODO: discuss (e.g. WGS)</LIBRARY_STRATEGY>
#                <LIBRARY_SOURCE>GENOMIC SINGLE CELL</LIBRARY_SOURCE>
#                <LIBRARY_SELECTION>TODO: discuss</LIBRARY_SELECTION>
#                <LIBRARY_LAYOUT>
#                    <PAIRED NOMINAL_LENGTH="TODO: did not see in JSON" NOMINAL_SDEV="TODO: did not see in JSON"/>
#                </LIBRARY_LAYOUT>
#            </LIBRARY_DESCRIPTOR>
#        </DESIGN>
#        <PLATFORM>
#            <ILLUMINA>
#                <INSTRUMENT_MODEL>TODO: instrument_manufacturer_model</INSTRUMENT_MODEL>
#            </ILLUMINA>
#        </PLATFORM>
#    </EXPERIMENT>
# </EXPERIMENT_SET>

_study_ref = None


def _add_experiment_xml(experiment_set_element, process_json):
    print(process_json)
    experiment_element = ET.SubElement(experiment_set_element, 'EXPERIMENT')
    title_element = ET.SubElement(experiment_element, 'TITLE')
    study_ref_element = ET.SubElement(experiment_element, 'STUDY_REF')
    design_element = ET.SubElement(experiment_element, 'DESIGN')
    design_description_element = ET.SubElement(design_element, 'DESIGN_DESCRIPTION')
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
    library_strategy_element.text = "RNA-Seq"
    library_source_element.text = "TRANSCRIPTOMIC SINGLE CELL"
    library_selection_element.text = "unspecified"
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


def convert(dataset_json):
    for element in dataset_json:
        if 'schema_type' in element:
            schema_type = element['schema_type']
            if schema_type == 'project':
                if 'content' in element:
                    project_set_xml = _create_project_set_xml(element['content'])
                    _output_xml("project", project_set_xml)
            if schema_type == 'biomaterial':
                if 'content' in element:
                    sample_set_xml = _create_sample_set_xml(element['content'])
                    _output_xml("sample", sample_set_xml)
            if schema_type == 'process':
                if 'content' in element:
                    experiment_set_xml = _create_experiment_set_xml(element['content'])
                    _output_xml("experiment", experiment_set_xml)


def _process_event(event):
    submission = json.loads(event["body"][0])
    return submission


def _output_xml(xml_type, xml_string):
    xml_str = minidom.parseString(xml_string).toprettyxml(indent="   ")
    with open("output/" + xml_type + ".xml", "w") as f:
        f.write(xml_str)
