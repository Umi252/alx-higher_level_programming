#!/usr/bin/python3

"""
This is the Square module.
It defines the Square class representing a square shape.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        :param size: The size of the square's sides.
        :type size: int, optional
        :param position: The position of the square.
        :type position: tuple, optional
        :raises TypeError: If size is not an integer.
        :raises ValueError: If size is less than 0.
        :raises TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        :return: The size of the square.
        :rtype: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        :param value: The size of the square's sides.
        :type value: int
        :raises TypeError: If value is not an integer.
        :raises ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        :return: The position of the square.
        :rtype: tuple
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        :param value: The position of the square.
        :type value: tuple
        :raises TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #.

        If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
