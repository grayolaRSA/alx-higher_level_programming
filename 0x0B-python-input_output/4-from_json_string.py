#!/usr/bin/python3
"""module for conversion of JSON strings"""


import json


def from_json_string(my_str):
    """
    function converts JSON string
    Return: Python object
    """

    return json.loads(my_str)
