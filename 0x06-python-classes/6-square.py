#!/usr/bin/python3
"""
This module contains the definition of the Square class.
"""


class Square:
    """
    Class that defines properties of a square.

    Attributes:
        size (int): The size of a square's side.
        position (tuple): The position of the square's top-left corner.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates a new instance of a square.

        Args:
            size (int): The size of the square's side. Default is 0.
            position (tuple): The position of the square's top-left corner. Default is (0, 0).
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The current square's area.
        """
        return self.size ** 2

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square's top-left corner.

        Returns:
            tuple: The position as a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square's top-left corner.

        Args:
            value (tuple): The new position as a tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square with the character '#'.

        If size is equal to 0, an empty line is printed.
        """
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
