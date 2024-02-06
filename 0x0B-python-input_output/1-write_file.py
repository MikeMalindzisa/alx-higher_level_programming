#!/usr/bin/python3
"""
This module defines a function to write a string to a text file (UTF8)
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of
    characters written.

    Args:
        filename (str): The name of the text file to write to.
        Default is an empty string.
        text (str): The string to write to the file.
        Default is an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
