#!/usr/bin/python3
"""Module for  adding attributes to objects"""


def add_attribute(obj, att, value):
    """
    Adds an attribute to object if possible
    Args:
        obj: Python object to add an attribute to
        att (str): Name of new attribute
        value: Attribute value
    Raises TypeError if attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
