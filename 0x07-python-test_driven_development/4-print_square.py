#!/usr/bin/python3
"""Function that prints a square made with '#' characters."""


def print_square(size):
    """
    Print a square made with '#' characters.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(1)
        #

        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        print("#" * size)
