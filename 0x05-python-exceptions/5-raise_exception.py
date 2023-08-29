#!/usr/bin/python3

def raise_exception():
    try:
        value = "string" + 5
    except TypeError as e:
        raise e

try:
    raise_exception()
except TypeError:
    print("Exception has been raised")
