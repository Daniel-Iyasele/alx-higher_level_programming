#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        length = len(my_list) - 1
        for i in range(length):
            if my_list[i] > my_list[i + 1]:
                max_no = my_list[i]
                my_list[i + 1] = max_no
        return max_no
