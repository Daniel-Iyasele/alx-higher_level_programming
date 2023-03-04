#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i, v in enumerate(my_list):
            if i == x:
                break
            else:
                print(v, end="")
                count += 1
        print()
        return count
    except UnknownError:
        print("Unknown error occured")
