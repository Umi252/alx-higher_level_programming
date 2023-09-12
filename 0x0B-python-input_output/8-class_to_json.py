#!/usr/bin/python3
"""
Returns a dictionary description
with simple data structures for JSON serialization of an object.
"""


def class_to_json(obj):
    """Converts attributes of an object to a dictionary for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object.
    """
    return obj.__dict__
