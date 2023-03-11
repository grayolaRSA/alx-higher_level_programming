#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_list.pop(idx)
        my_list.insert(idx - 1, element)
        return my_list
    else:
        return my_list
