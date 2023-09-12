#!/usr/bin/python3
"""Defines a function that converts an object to a JSON string."""


import json


def to_json_string(my_obj):
    """Converts an object to a JSON string.

    Args:
        my_obj: The object to be converted.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
