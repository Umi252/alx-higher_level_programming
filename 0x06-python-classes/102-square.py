#!/usr/bin/python3

class Square:
    """
    Represents a square with size attribute.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (float or int): The size of the square's sides (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Args:
            value (float or int): The size value to set.

        Raises:
            TypeError: If the value is not a number (float or integer).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Equality operator.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality operator.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than operator.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal operator.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than operator.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal operator.
        """
        return self.area() >= other.area()
