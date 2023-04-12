#!/usr/bin/python3
"""module for reading file"""


def read_file(filename=""):
    """
    function reads text file
    prints it to stdout
    Format = UTF8
    """
    with open(filename, encoding='utf-8') as f:
        read_file = f.read()
        print(read_file)
