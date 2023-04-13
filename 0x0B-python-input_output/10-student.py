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

    def to_json(self, attrs=None):
        """
        returns dictionary representation of student instance
        where attrs is list of strings, only attributes from list
        to be retrieved
        """
        if attrs is None:
            return self.__dict__
        std_dict = {}
        for j in attrs:
            if j in self.__dict__ and type(self.__dict__[j]) is str:
                std_dict[j] = self.__dict__[j]
        return std_dict
