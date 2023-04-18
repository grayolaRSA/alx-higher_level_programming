#!/usr/bin/python3
"""test module for base class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """
    class for testing base class
    """
    @classmethod
    def setUpClass(cls):
        """class method called before tests"""
        Base.id = None

    @classmethod
    def tearDownClass(cls):
        """remove the files created in the test"""
        os.remove("Rectangle.json")

    def test_to_json_string(self):
        # test the case using an empty string
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        """
        test save_to_file method in base class
        -creates file that needs to be removed by tear down class
        """
        # Create some rectangle objects to save to file
        r1 = Rectangle(10, 20)
        rect_list = [r1]

        # Call the save_to_file method to save the rectangles to a file
        Rectangle.save_to_file(rect_list)

        # Verify that the file was created and contains the expected data
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        expected_contents = (
            '[{"id": 1, "width": 10, "height": 20, "x": 0, "y": 0}]')

        self.assertEqual(file_contents, expected_contents)


if __name__ == '__main__':
    unittest.main()
