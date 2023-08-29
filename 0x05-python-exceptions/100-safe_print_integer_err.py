#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        print("Exception:", e, file=sys.stderr)
        return False

if __name__ == "__main__":
    value = 89  # Replace this with an integer value
    result = safe_print_integer_err(value)
    print(result)
