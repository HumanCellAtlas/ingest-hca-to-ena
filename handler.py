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


def add_project_xml(project_set_element, project_json):
    project_element = ET.SubElement(project_set_element, 'PROJECT')
    name_element = ET.SubElement(project_element, 'NAME')
    title_element = ET.SubElement(project_element, 'TITLE')
    description_element = ET.SubElement(project_element, 'DESCRIPTION')
    submission_project_element = ET.SubElement(project_element, 'SUBMISSION_PROJECT')
    ET.SubElement(submission_project_element, 'SEQUENCING_PROJECT')
    if 'project_core' in project_json:
        project_core = project_json['project_core']
        if 'project_shortname' in project_core:
            name_element.text = project_core['project_shortname']
        if 'project_title' in project_core:
            title_element.text = project_core['project_title']
        if 'project_description' in project_core:
            description_element.text = project_core['project_description']


def create_project_set_xml(projects_json):
    project_set_element = ET.Element('PROJECT_SET')
    for project_json in projects_json:
        add_project_xml(project_set_element, project_json)
    project_set_xml = ET.tostring(project_set_element)
    return project_set_xml


def output_xml(xml_type, xml_string):
    print(xml_type + ":\n" + str(xml_string))
    xml_str = minidom.parseString(xml_string).toprettyxml(indent="   ")
    with open(xml_type + ".xml", "w") as f:
        f.write(xml_str)


def convert(dataset_json):
    for element in dataset_json:
        if 'schema_type' in element:
            schema_type = element['schema_type']
            if schema_type == 'project':
                if 'content' in element:
                    project_set_xml = create_project_set_xml(element['content'])
                    output_xml("project", project_set_xml)


def _process_event(event):
    submission = json.loads(event["body"][0])
    return submission
