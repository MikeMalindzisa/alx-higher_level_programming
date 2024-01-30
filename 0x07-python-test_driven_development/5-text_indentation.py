#!/usr/bin/python3
"""
Function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Do hard things! Are you ready? I bet you are.")
        Do hard things!

        Are you ready?

        I bet you are.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    current_line = ""
    for character in text:
        current_line += character
        if character in ('.', ':', '?'):
            print(f"{current_line.strip()}\n")
            current_line = ""
