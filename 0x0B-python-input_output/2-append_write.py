#!/usr/bin/python3
"""
This module defines a function to append a string to the end
of a text file (UTF8) and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8)
    and return the number of characters added.

    Args:
        filename (str): The name of the text file to append to.
        Default is an empty string.
        text (str): The string to append to the file. Default is
        an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added


if __name__ == "__main__":
    nb_characters_added = append_write("file_append.txt",
                                       "This School is so cool!\n")
    print(nb_characters_added)
