#!/usr/bin/python3
def max_integer(my_list=[]):
    max_no = 0
    if len(my_list) == 0:
        return None
    for i, n in enumerate(my_list):
        if i == 0 or n >= max_no:
            max_no = n
    return max_no
