#!/usr/bin/python3
"""module that saves object to file"""


import json


def save_to_json_file(my_obj, filename):
    """
    function writes object to file

    Args:
    my_obj: object
    filename: file

    Return:
    Nothing
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
