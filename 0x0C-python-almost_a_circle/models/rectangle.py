#!/usr/bin/python3
"""module for rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class
    inherits from base class
    Args:
    width(int): width of rectangle
    height(int): height of rectangle
    x(int): cartesian positional attribute
    y(int): cartesian positional attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialising attributes
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            calculates area of rectangle
            args:
            width
            height
            Return
            area(int): area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        prints rectangles in stdout with # characters
        """
        for j in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for p in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        string special method for rectangle class
        """
        str_rctngl = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_yx = "{}/{} - ".format(self.x, self.y)
        str_hw = "{}/{}".format(self.width, self.height)

        return str_rctngl + str_id + str_yx + str_hw

    def update(self, *args, **kwargs):
        """
        method to update Rectangle class using *args
        """
        r_args = ('id', 'width', 'height', 'x', 'y')
        for arg in range(len(args)):
            setattr(self, r_args[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        method for dictionary representation of rectangle
        """
        r_atr = ['id', 'width', 'height', 'x', 'y']
        dict_atr = {}

        for key in r_atr:
                dict_atr[key] = getattr(self, key)

        return dict_atr
