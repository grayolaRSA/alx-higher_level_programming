#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = None
    if len(my_list) > 0:
        max_value = sorted(my_list)[-1]
    return max_value
