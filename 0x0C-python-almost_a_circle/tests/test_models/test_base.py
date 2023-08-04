#!/usr/bin/python3
"""test module for base class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_to_json_string(self):
        """test for json string function"""
        s1 = {"id": 1, "width": 2, "height": 3}
        s2 = {"id": 4, "width": 5, "height": 6}

        # test the case using an empty string
        self.assertEqual(Base.to_json_string([]), "[]")

        json_string = Base.to_json_string([s1, s2])
        self.assertIsInstance(json_string, str)

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
            '[{"id": 9, "width": 10, "height": 20, "x": 0, "y": 0}]')

        self.assertEqual(file_contents, expected_contents)

    def test_create(self):
        """test method to test create method"""
        r1 = Rectangle(10, 7, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """test method to test load_from_file method"""
        b1 = Rectangle(3, 4, 2, 8)
        b2 = Rectangle(2, 4)
        Rectangle.save_to_file([b1, b2])
        t = Rectangle.load_from_file()
        self.assertIsInstance(t, list)

    def test_save_to_file_csv(self):
        """test method to test save_to_file_csv method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            r = csv.reader(f)
            for row in r:
                self.assertEqual(row, ['1', '10', '7', '2', '8'])
                self.assertEqual(next(r), ['2', '2', '4', '0'])

    def test_load_from_file_csv(self):
        """test method to test load_from_file_csv method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        t = Rectangle.load_from_file_csv()
        self.assertIsInstance(t, list)


if __name__ == '__main__':
    unittest.main()
