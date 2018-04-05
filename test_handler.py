import json
import unittest
import uuid

from io import StringIO

from lxml import etree

from handler import convert
from handler import zipdir


def validate_output(schema_file_name, xml_file_name, job_id):
    # with open("/tmp/" + job_id + "/" + xml_file_name, 'r') as xml_file:
    with open("examples/tmp/" + job_id + "/" + xml_file_name, 'r') as xml_file:
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
        # with open('examples/metadata_spleen_v5_20180313_userFriendlyHeaders.json') as json_data:
        with open('examples/preview_release/MSS/bundle.json') as json_data:
            job_id = str(uuid.uuid1())
            dataset_json = json.load(json_data)
            convert(dataset_json, job_id)
            zipdir(job_id)
            validate_output("SRA.submission.xsd", "submission.xml", job_id)
            validate_output("ENA.project.xsd", "project.xml", job_id)
            validate_output("SRA.sample.xsd", "sample.xml", job_id)
            validate_output("SRA.experiment.xsd", "experiment.xml", job_id)
            validate_output("SRA.run.xsd", "run.xml", job_id)


if __name__ == '__main__':
    unittest.main()
