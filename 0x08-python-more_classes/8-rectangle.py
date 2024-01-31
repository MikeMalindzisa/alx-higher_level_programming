#!/usr/bin/python3
"""Rectangle class

This module defines the Rectangle class, which represents a geometric rectangle.
"""


class Rectangle:
    """A class to represent rectangles.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): Class attribute to count the number of instances created.
        print_symbol (str): Class attribute for the symbol used in the __str__ representation.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with specified width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        """Return the rectangle with the bigger or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the bigger or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle using the specified print symbol.
        """
        if not self.perimeter():
            return ""
        return '\n'.join("{}".format(self.print_symbol) * self.width for _ in range(self.height))

    def __repr__(self):
        """Return a string representation of the rectangle for debugging.

        Returns:
            str: A representation of the rectangle that can be used to recreate it.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Handle deletion of the rectangle instance.

        Decreases the number of instances when an instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

