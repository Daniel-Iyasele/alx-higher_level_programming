#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char >= 'A' and char <= 'Z':
            print("{}".format(char))
        else:
            print("{}".format(chr(ord(char) - 32)))
