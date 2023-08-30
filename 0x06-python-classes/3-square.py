#!/usr/bin/python3
"""
This module contains the definition of the Square class.
"""


class Square:
    """
    This class represents a square.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Default is 0.

        Attributes:
            __size (int): The size of the square (private attribute).
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
