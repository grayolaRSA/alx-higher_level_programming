#!/usr/bin/python3
"""
A module to print either full names or first names.
The last name is optional
"""


def say_my_name(first_name, last_name=""):
    """function prints name arguments passed"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name:
        print(f'My name is {first_name} {last_name}')
    else:
        print(f'My name is {first_name}')
