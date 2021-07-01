#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import pep8


class TestFileStorage(unittest.TestCase):

    def test_pep8_Filestorage(self):
        pep8style = pep8.\
                        Checker("models/engine/file_storage", source_code=True)
        result = pep8style.check_all()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
