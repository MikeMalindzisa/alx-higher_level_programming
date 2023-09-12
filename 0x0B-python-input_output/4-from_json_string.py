#!/usr/bin/python3
import json

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
    return json.loads(my_str)
