#!/usr/bin/python3
"""
This module defines the `lookup` function.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the attributes and
        methods of the object.
    """
    return dir(obj)
