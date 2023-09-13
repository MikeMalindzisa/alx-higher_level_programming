#!/usr/bin/python3

"""
This module contains a class Square that inherits from Rectangle
(9-rectangle.py). (task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.

    Attributes:
        None

    Methods:
        __init__(self, size): Initializes a Square instance with a size.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
