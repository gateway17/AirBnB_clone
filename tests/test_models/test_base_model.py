#!/usr/bin/python3
"""model unitest for base model"""
from models.base_model import BaseModel
import unittest
import pep8


class TestBaseModel(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.Checker("models/base_model", source_code=True)
        result = pep8style.check_all()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
