#!/usr/bin/python3
"""module for defining Student class"""


class Student:
    """
    class to define student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialising instance variables

        Args:
        first_name(str): first name
        last_name(str): last name
        age(int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        class method returns dictionary representation of
        student instance
        """
        json_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return json_dict
