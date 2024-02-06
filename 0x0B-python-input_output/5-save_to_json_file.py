#!/usr/bin/python3
"""
This module defines a function to write an object to a
text file using its JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the text file to save the JSON
        representation to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
