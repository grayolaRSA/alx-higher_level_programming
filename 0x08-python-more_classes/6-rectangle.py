#!/usr/bin/python3
""" Class that defines a rectangle"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """intialises a rectangle
        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets value of width(int)
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        changes the value of the width
        Args:
        value(int): new value of width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets value of rectangle height (int)
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
            changes the value of the rectangle height
            Args:
            value(int): new value of height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            returns the rectangle area
        """

        return self.height * self.width

    def perimeter(self):
        """
            returns the rectangle perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Method that prints out the rectangle"""

        rectangle_print = ""

        if self.width == 0 or self.height == 0:
            return rectangle_print
        for i in range(self.__height):
            rectangle_print += "#" * self.width + "\n"
        return rectangle_print[:-1]

    def __repr__(self):
        """
        method that prints or evals an
        internal representation of rectangle
        """

        a = str(self.__width)
        b = str(self.__height)

        rect = "Rectangle(" + a + ", " + b + ")"
        return rect

    def __del__(self):
        """
        method that deletes an instance
        of a rectangle
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
