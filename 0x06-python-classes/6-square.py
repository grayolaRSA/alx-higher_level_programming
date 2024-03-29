#!/usr/bin/python3
"""A module containing a square"""


class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes square
        Args:
            size (int): size of the square
        position(tuple): position of the square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets value of size
        Returns:
            size (int)
        """

        return self.__size

    @size.setter
    def size(self, value):
        """ Change the value of size
        Args:
            value (int): new value of size
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets position of square
        Returns:
        #
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Change the position of square
            Args:
            value (tuple): new position of square
            """
        if not isinstance(value, tuple) and len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(n, (int)) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):

        """ Calculates the area of a square
                Returns:
                area
                """

        return self.__size ** 2

    def my_print(self):

        """ Prints out the square"""

        if self.__size == 0:
            print("")

        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print("", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
