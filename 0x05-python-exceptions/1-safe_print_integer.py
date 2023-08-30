#!/usr/bin/python3


def safe_print_integer(value):
    """
    Safely prints an integer using the "{:d}".format() method.

    Args:
        value: The value to be printed, which can be of any type.

    Returns:
        bool: True if value is an integer and has been printed,
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
