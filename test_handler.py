import unittest
import json
from handler import convert


class TestHandler(unittest.TestCase):

    def test_convert(self):
        with open('examples/metadata_spleen_v5_20180313_userFriendlyHeaders.json') as json_data:
            dataset_json = json.load(json_data)
            convert(dataset_json)


if __name__ == '__main__':
    unittest.main()
