#!/usr/bin/python3

"""
This module contains a function for checking if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class; otherwise, False.
    """
    return type(obj) == a_class
