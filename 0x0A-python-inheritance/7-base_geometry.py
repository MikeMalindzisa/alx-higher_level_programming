#!/usr/bin/python3

"""
This module contains a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    Base class for geometry.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the message "area() is
        not implemented."
        integer_validator(self, name, value): Validates the given
        integer value.
    """

    def area(self):
        """
        Raise an Exception indicating that the area() method is
        not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated
            (always a string).
            value (int): The integer value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
