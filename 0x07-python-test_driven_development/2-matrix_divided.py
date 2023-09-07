#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor and round to 2 decimal places.

    Args:
        matrix (list of lists): The input matrix,
        where each row should have the same size.
        div (int or float): The divisor, which can't be 0.

    Returns:
        list of lists: A new matrix with elements divided by div and
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """
    # Check if div is a number (integer or float)
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists of integers or floats
    if not all(
        isinstance(row, list) and all(isinstance(x, (int, float)) for x in row)
        for row in matrix
    ):
        raise TypeError
    ("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [
        [round(x / div, 2) for x in row]
        for row in matrix
    ]

    return new_matrix
