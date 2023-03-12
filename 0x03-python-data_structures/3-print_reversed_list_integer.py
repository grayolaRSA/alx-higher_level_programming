#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for idx, element in enumerate(reversed(my_list)):
        print("{:d}".format(element))
