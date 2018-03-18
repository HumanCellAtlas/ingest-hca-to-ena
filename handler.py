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

# <SAMPLE_SET>
#   <SAMPLE alias="TODO: biomaterial_id">
#     <TITLE>TODO: e.g. biomaterial_name (biomaterial_description)</TITLE>
#     <SAMPLE_NAME>
#       <TAXON_ID>TODO: ncbi_taxon_id</TAXON_ID>
#     </SAMPLE_NAME>
#     <SAMPLE_ATTRIBUTES>
#       <SAMPLE_ATTRIBUTE>
#         <TAG>cause_of_death</TAG>
#         <VALUE>Hypoxic brain damage</VALUE>
#       </SAMPLE_ATTRIBUTE>
#       ...
#     </SAMPLE_ATTRIBUTES>
#   </SAMPLE>
# </SAMPLE_SET>

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


def _output_xml(xml_type, xml_string):
    xml_str = minidom.parseString(xml_string).toprettyxml(indent="   ")
    with open("output/" + xml_type + ".xml", "w") as f:
        f.write(xml_str)


def _create_sample_set_xml(biomaterials_json):
    sample_set_element = ET.Element('SAMPLE_SET')
    for biomaterial_json in biomaterials_json:
        _add_sample_xml(sample_set_element, biomaterial_json)
    sample_set_xml = ET.tostring(sample_set_element)
    return sample_set_xml


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


def _process_event(event):
    submission = json.loads(event["body"][0])
    return submission
