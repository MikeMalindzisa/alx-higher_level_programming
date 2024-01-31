#!/usr/bin/python3
"""Rectangle class

This module defines the Rectangle class, which represents a geometric rectangle.
"""


class Rectangle:
    """A class to represent rectangles.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with specified width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): The width to set for the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('Width must be an integer')
        if value < 0:
            raise ValueError('Width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): The height to set for the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('Height must be an integer')
        if value < 0:
            raise ValueError('Height must be >= 0')
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle using '#' symbols.
        """
        if not self.perimeter():
            return ""
        return '\n'.join('#' * self.width for _ in range(self.height))

