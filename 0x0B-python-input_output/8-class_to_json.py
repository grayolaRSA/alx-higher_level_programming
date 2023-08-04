#!/usr/bin/python3
"""Module for defining a Python class to JSON function"""


def class_to_json(obj):
    """
    Function that returns the dictionary representation
    of a simple data structure
    Args:
    obj: Python object
    Return:
    JSON function
    """
    return obj.__dict__
