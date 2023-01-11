#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for ch in range(len(my_string)):
        if my_string[ch] == 'c' or my_string[ch] == 'C':
            ch += 1
        else:
            new = new + my_string[ch]
    return new
