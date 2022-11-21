import unittest
import os
import json
from app import create_app
from app import length_review,lenght_title


class ApiTestCase(unittest.TestCase):
    """ This class represents the api test """

    def test_length_review(self):
        self.assertEqual(3, length_review('FOO'))

    def test_lenght_title(self):
        self.assertEqual(3, length_review('FOO'))


if __name__ == '__main__':
    unittest.main()
