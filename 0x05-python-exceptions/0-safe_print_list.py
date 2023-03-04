#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new = []
    try:
        for i, v in enumerate(my_list):
            if i == x:
                break
            else:
                print(v, end="")
        print()
        return v
    except UnknownError:
        print("Unknown error occured")
