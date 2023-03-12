#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = 0
    my_list.reverse()
    for idx in range(len(my_list)):
        print("{:d}".format(my_list[idx]))
