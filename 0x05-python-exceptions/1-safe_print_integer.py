#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value:
            print("{:d}".format(value))
            return True
        else:
            return False
        print()
    except NameError:
        return False
    except ValueError:
        return False
