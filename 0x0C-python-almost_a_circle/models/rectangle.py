#!/usr/bin/python3
"""Module with the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle initialization with width, height, and offsets.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): Width offset for drawing the rectangle.
            y (int): Height offset for drawing the rectangle.
            id: Identifier for the instance. If None, then object count is used.

        Raises:
            TypeError: If `width`, `height`, `x`, or `y` are not ints.
            ValueError: If `width` or `height` are <= 0, or `x` or `y` are < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter/setter for width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width property."""
        self._validate_positive_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter/setter for height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height property."""
        self._validate_positive_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter/setter for x (offset) property."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x (offset) property."""
        self._validate_non_negative_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter/setter for y (offset) property."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y (offset) property."""
        self._validate_non_negative_int("y", value)
        self.__y = value

    def area(self):
        """Compute the area of a rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print a representation of a rectangle to stdout."""
        print('\n' * self.__y +
              '\n'.join([' ' * self.__x + '#' * self.__width
                         for _ in range(self.__height)]))

    def __str__(self):
        """Return a string representation of a Rectangle instance."""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Update Rectangle instances with *args and **kwargs."""
        attrs = ["id", "width", "height", "x", "y"]
        for attr, arg in zip(attrs, args):
            setattr(self, attr, arg)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """Return dictionary representation of writable attributes."""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }

    @staticmethod
    def _validate_positive_int(name, value):
        """Validate that a value is a positive integer."""
        if not isinstance(value, int) or value <= 0:
            raise TypeError(f"{name} must be a positive integer")

    @staticmethod
    def _validate_non_negative_int(name, value):
        """Validate that a value is a non-negative integer."""
        if not isinstance(value, int) or value < 0:
            raise TypeError(f"{name} must be a non-negative integer")

