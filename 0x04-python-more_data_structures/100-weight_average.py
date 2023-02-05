#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    mult = 0
    weight = 0
    for i in range(len(my_list)):
        for j in range(len(my_list[0])):
            if (j + 1) < len(my_list[0]):
                mult += my_list[i][j] * my_list[i][j + 1]
                weight += my_list[i][j + 1]
    average = mult / weight
    return average
