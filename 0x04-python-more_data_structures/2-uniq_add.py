#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    u_list = []
    for item in my_list:
        if item not in u_list:
            u_list.append(item)
    for n in range(len(u_list)):
        result += u_list[n]
    return result
