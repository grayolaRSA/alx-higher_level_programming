#!/usr/bin/python3
"""module for writing to file"""


def write_file(filename="", text=""):
    """
    function writes to file
    creates file if not existent
    returns number of characters
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
