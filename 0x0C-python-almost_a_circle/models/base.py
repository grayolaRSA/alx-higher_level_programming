#!/usr/bin/python3
"""module for base class"""


class Base:
    """
    base class for all other classes
    Args:
    nb_objects(int): number of objects
    id(int): identifier of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialise instances
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
