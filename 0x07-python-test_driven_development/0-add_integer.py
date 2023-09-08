#!/usr/bin/python3
"""Define function add_integer."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Prototype:
    def add_integer(a, b=98):

    Args:
        a (int or float): The first integer.
        b (int or float, optional): The second integer. Defaults to 98.

    Returns:
        int: The addition of `a` and `b`.

    Raises:
        TypeError: If `a` or `b` are not integers or floats.

    This function takes two arguments, `a` and `b`, and adds
    them together. If `a` or `b` are floats,
    they are first casted to integers. If either `a` or `b` is not
    a valid type, a TypeError is raised.
    """
    if ((type(a) != int) and (type(a) != float)):
        raise TypeError("a must be an integer")
    if ((type(b) != int) and (type(b) != float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
