#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    for i in range(len(my_list)):
        if i < 0 or i >= len(my_list):
            return my_list
        else:
            if i != idx:
                new_list.append(my_list[i])
    return new_list
