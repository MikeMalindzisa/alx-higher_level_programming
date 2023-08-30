#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    Represents a square with various properties and methods.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple): The position of the square's top-left corner.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides. Default is 0.
            position (tuple): The position of the square's top-left corner.
                             Default is (0, 0).
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

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

    @property
    def position(self):
        """
        Retrieves the position of the square's top-left corner.

        Returns:
            tuple: The position as a tuple (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square's top-left corner.

        Args:
            value (tuple): The new position as a tuple (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not
            all(isinstance(coord, int) and coord >= 0 for coord in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square using '#' characters.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Converts the square to a string for printing.

        Returns:
            str: The square pattern as a string.
        """
        result = []
        for _ in range(self.position[1]):
            result.append("")

        for _ in range(self.size):
            result.append(" " * self.position[0] + "#" * self.size)

        return "\n".join(result)
