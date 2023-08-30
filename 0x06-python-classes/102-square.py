#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    Represents a square with various properties and methods.

    Attributes:
        size (float or int): The size of the square's sides.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (float or int): The size of the square's sides. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The new size value.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.size ** 2

    def __lt__(self, other):
        """
        Less than operator.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if the area of the current square is less than
                  the area of the other square, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal operator.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if the area of the current square is less than
                  or equal to the area of the other square, False otherwise.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """
        Equal operator.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if the area of the current square is equal to
                  the area of the other square, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not equal operator.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if the area of the current square is not equal to
                  the area of the other square, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than operator.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if the area of the current square is greater than
                  the area of the other square, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal operator.

        Args:
            other (Square): The other Square instance.

        Returns:
            bool: True if the area of the current square is greater than
                  or equal to the area of the other square, False otherwise.
        """
        return self.area() >= other.area()
