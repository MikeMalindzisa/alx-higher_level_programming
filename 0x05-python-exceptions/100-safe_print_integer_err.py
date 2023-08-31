#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Prints an integer or raises an exception with an error message.

    Args:
        value: The value to be printed.

    Returns:
        bool: True if the value is an integer and printed successfully,
              False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception:", e, file=sys.stderr)
        return False
