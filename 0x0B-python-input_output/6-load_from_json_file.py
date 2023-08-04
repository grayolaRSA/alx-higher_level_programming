#!/usr/bin/python3
"""module for creation of object from JSON file"""


import json


def load_from_json_file(filename):
    """
    function creates Python object from JSON file

    Args:
    filename: JSON file

    Return:
    Python object
    """
    with open(filename, 'r', encoding='utf-8') as file:
        obj = file.read()
        return json.loads(obj)
