#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    test_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            test_list.append(True)
        else:
            test_list.append(False)
    return test_list
