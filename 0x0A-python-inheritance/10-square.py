#!/usr/bin/python3

"""
This module contains a class Square that inherits from Rectangle
(9-rectangle.py).
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
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
