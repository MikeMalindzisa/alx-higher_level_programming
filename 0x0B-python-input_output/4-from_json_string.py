#!/usr/bin/python3
from json import loads as str_load

"""
This module defines a function to parse a JSON string and
return the corresponding Python data structure.
"""


def from_json_string(my_str):
    """
    Parse a JSON string and return the corresponding
    Python data structure.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return str_load(my_str)
