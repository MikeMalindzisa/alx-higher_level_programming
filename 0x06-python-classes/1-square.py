#!/usr/bin/python3
"""
This module contains the definition of the Square class.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square (private attribute).
        """
        self.__size = size
