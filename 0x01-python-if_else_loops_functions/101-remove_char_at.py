#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for char in range(len(str)):
        if char == n:
            char = n + 1
            continue
        else:
            new = new + str[char]
    return new
