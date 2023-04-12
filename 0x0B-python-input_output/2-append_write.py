#!/usr/bin/python3
"""module that appends string to file"""


def append_write(filename="", text=""):
    """
    function appends string to file
    returns number of char added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
