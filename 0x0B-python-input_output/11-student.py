#!/usr/bin/python3
"""
Defines a Student class.
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attributes to retrieve.
                Defaults to None.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }

        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
