#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if char >= 'A' and char <= 'Z':
            print("{}".format(char), end="")
        else:
            print("{}".format(chr(ord(char) - 32)), end="")
