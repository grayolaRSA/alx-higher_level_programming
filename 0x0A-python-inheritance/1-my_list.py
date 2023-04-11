#!/usr/bin/python3
"""module prints a list"""


class MyList(list):
    """
    sub-class of list class
    """

    def print_sorted(self):
        """Print the sorted list"""
        print (sorted(self))
