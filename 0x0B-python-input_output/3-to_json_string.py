#!/usr/bin/python3
"""module for JSON"""


def to_json_string(my_obj):
    """
    function for turning object into JSON string
    """
    import json

    return json.dumps(my_obj)
