#!/usr/bin/python3
"""Module that defines a Base class."""


class Base:
    """Represents the base of all classes in the project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the Base class.

        Args:
            id (int, optional): The ID of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
