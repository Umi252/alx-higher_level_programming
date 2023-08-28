#!/usr/bin/python3

def raise_exception():
    try:
        value = "string" + 5
    except TypeError as e:
        print("Type error occurred:", e)

raise_exception()

