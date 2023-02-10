#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary)
    for k in range(len(keys)):
        if k < len(keys) and a_dictionary[keys[k]] == value:
            del a_dictionary[keys[k]]
    return a_dictionary
