import json
import unittest
from io import StringIO

from lxml import etree

from handler import convert


def validate_output(schema_file_name, xml_file_name):
    with open("output/" + xml_file_name, 'r') as xml_file:
        xml_to_check = xml_file.read()
    with open("xml_schemas/" + schema_file_name) as xsd_file:
        xml_schema_doc = etree.parse(xsd_file)
        xml_schema = etree.XMLSchema(xml_schema_doc)
    try:
        xml_doc = etree.parse(StringIO(xml_to_check))
        xml_schema.assertValid(xml_doc)
    except IOError:
        print('Invalid File')
        quit()
    except etree.XMLSyntaxError as err:
        print('XML Syntax Error, see error_syntax.log')
        with open('error_syntax.log', 'w') as error_log_file:
            error_log_file.write(str(err.error_log))


class TestHandler(unittest.TestCase):

    def test_convert(self):
        with open('examples/metadata_spleen_v5_20180313_userFriendlyHeaders.json') as json_data:
            dataset_json = json.load(json_data)
            convert(dataset_json)
            validate_output("ENA.project.xsd", "project.xml")
            validate_output("SRA.sample.xsd", "sample.xml")
            validate_output("SRA.experiment.xsd", "experiment.xml")


if __name__ == '__main__':
    unittest.main()
