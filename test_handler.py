import unittest
import json
from handler import convert

class TestHandler(unittest.TestCase):

    def test_convert(self):
        res = convert(None, None)
        self.assertEquals(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

if __name__ == '__main__':
    unittest.main()