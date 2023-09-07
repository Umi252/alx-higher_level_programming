#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer
        or float. Defaults to 98.

    Returns:
        int: The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or a float.

    Example:
        >>> add_integer(5, 3)
        8
        >>> add_integer(5.0, 3.5)
        8
    """
    # Check if a and b are either integers or floats
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    # Perform the addition and return the result
    return int(a + b)


if __name__ == "__main__":
    result = add_integer(5, 3)
    print(result)
