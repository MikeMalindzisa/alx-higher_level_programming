#!/usr/bin/python3

"""
This module contains a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    MyInt class that inherits from int and inverts the == and != operators.

    Attributes:
        None

    Methods:
        __eq__(self, other): Inverts the == operator.
        __ne__(self, other): Inverts the != operator.
    """

    def __eq__(self, other):
        """
        Invert the == operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert the != operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)
