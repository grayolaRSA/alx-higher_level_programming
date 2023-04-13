#!/usr/bin/python3
"""Module for rectangle class that inherits from base geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        sub-class of Base Geometry
        defines a rectangle
        Args:
        width(int)
        height(int)
    """

    def __init__(self, width, height):
        """
            initialise variables
            width(int)
            height(int)
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculate area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """
            Print the representation of a Rectangle
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
