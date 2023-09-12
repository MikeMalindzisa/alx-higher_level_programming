#!/usr/bin/python3
"""
This module defines a function to read and print the contents of
a text file to stdout.
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file to stdout.

    Args:
        filename (str): The name of the text file to read (UTF8).
        Default is an empty string.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
