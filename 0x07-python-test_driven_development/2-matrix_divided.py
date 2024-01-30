#!/usr/bin/python3
"""Define function matrix_divided."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix represented as a list of lists
        containing integers or floats.
        div (int or float): The number to divide all elements of the matrix by.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal
        places after division.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Example:
        >>> matrix = [
        ...     [1, 2, 3],
        ...     [4, 5, 6]
        ... ]
        >>> matrix_divided(matrix, 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    # Check if the input matrix is None, and if so, raise a TypeError
    if matrix is None:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if the divisor (div) is None, and if so, raise a TypeError
    if div is None:
        raise TypeError("div must be a number")

    # Check if all elements of the input matrix are either integers or floats
    if not all(isinstance(row, list) and all(
            isinstance(element, (int, float)) for element in row) for row in
               matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if the divisor is zero, and if so, raise a ZeroDivisionError
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in
                  matrix]

    return new_matrix
