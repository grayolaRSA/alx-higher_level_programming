#!/usr/bin/python3
"""Module for square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class for square
    Args:
    Size: size of square
    """
    def __init__(self, size):
        """
        instantiation of square variables
        Variable:
        Size(int)
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
