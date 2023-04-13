#!/usr/bin/python3
"""Module for base geometry class"""


class BaseGeometry:
    """Class to define base geometry attributes"""

    def area(self):
        """method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that validates variables
        Args:
        name: string variable
        value: integer variable that is to be validated
        """

        def __init__(self, name, value):
            """Initialise integer validator
            Args:
            name(str): name of tuple, list or dict entry
            value(int): value contained in entry
            """
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer".format(name))
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")
