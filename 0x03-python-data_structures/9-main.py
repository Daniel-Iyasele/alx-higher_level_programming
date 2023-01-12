#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
m = [3, 6, 1, 9, 12, -13, 78, 12, 1, 1, 5]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
print("Max: {}".format(max_integer(m)))  
