#!/usr/bin/python3
import math


class MagicClass:
    """
    A class that represents a magic circle with radius-related calculations.

    Attributes:
        radius (int or float): The radius of the magic circle.

    Methods:
        __init__(self, radius=0): Initializes a new MagicClass instance.
        area(self): Calculates the area of the magic circle.
        circumference(self): Calculates the circumference of the magic circle.
    """
    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (int or float): The radius of the magic circle.
        """
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
