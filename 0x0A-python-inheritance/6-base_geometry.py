#!/usr/bin/python3

"""
This module contains a class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """
    Base class for geometry.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented."
    """

    def area(self):
        """
        Raise an Exception indicating that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")
