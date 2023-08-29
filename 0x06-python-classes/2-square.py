#!/usr/bin/python3

"""
This is the Square module.
It defines the Square class representing a square shape.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        :param size: The size of the square's sides.
        :type size: int, optional
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
