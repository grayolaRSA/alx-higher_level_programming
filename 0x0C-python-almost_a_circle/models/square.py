#!/usr/bin/python3
"""a module for the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square defining class
    Args:
    size(int): size of square
    x(int): cartesian x coordinate
    y(int): cartesian y coordinate
    id(int): class id inherited from base class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialise attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        string special method for square class
        """
        str_sqr = "[Square]"
        str_id = " ({})".format(self.id)
        str_yx = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.width)

        return str_sqr + str_id + str_yx + str_size

    def update(self, *args, **kwargs):
        """
        method to update square class using *args and **kwargs
        -use of args or kwargs depends on conditions
        """
        if args:
            r_args = ('id', 'size', 'x', 'y')
            for i, arg in enumerate(args):
                    setattr(self, r_args[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            pass

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        sq_atr = ['id', 'size', 'x', 'y']

        return {key: getattr(self, key) for key in sq_atr}
