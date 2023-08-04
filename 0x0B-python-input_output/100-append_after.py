#!/usr/bin/python3
"""Module for a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): Name of file
        search_string (str): String to be searched for within the file
        new_string (str): String to be inserted
    """
    string = ""
    with open(filename) as f:
        for line in f:
            string += line
            if search_string in line:
                string += new_string
    with open(filename, "w") as w:
        w.write(string)
