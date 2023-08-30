#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    Represents a square with various properties and methods.

    Attributes:
        size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0): Initializes a new square instance.
        area(self): Calculates the area of the square.
        size(self): Gets the size of the square.
        size(self, value): Sets the size of the square.
        my_print(self): Prints the square pattern using '#'.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints the square using "#" characters.
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
