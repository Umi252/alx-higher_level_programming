#!/usr/bin/python3

"""
This is the Square module.
It defines the Square class representing a square shape.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        :param size: The size of the square's sides.
        :type size: int
        """
        self.__size = size
