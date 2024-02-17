#!/usr/bin/python3
"""Module containing Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square derived from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new square.

        Args:
            size (int): Side length of the square.
            x (int): Horizontal offset for drawing the square.
            y (int): Vertical offset for drawing the square.
            id: Identifier for the instance. If None, then object count.

        Raises:
            TypeError: If arguments are not integers (or None for id).
            ValueError: If size is <= 0 or x, y are < 0 or id < 0.
        """
        super().__init__(size, size, x=x, y=y, id=id)

    @property
    def size(self):
        """Getter/setter for the size property."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size property.

        Args:
            value (int): New size for the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is not positive.
        """
        self._validate_positive_int("size", value)
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size
        )

    def update(self, *args, **kwargs):
        """Update Square instance with provided arguments and keyword arguments.

        Args:
            *args: Positional arguments in the order 'id', 'size', 'x', 'y'.
            **kwargs: Keyword arguments for updating attributes.

        Example:
            >>> square = Square(1)
            >>> square.update(6, size=4, y=3)
            >>> print(square)
            [Square] (6) 0/3 - 4
        """
        attrs = ["id", "size", "x", "y"]
        for attr, arg in zip(attrs, args):
            setattr(self, attr, arg)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """Return dictionary representation of writable attributes.

        Returns:
            dict: Dictionary containing 'id', 'size', 'x', and 'y' attributes.
        """
        attrs = ["id", "size", "x", "y"]
        return {k: getattr(self, k) for k in attrs}

