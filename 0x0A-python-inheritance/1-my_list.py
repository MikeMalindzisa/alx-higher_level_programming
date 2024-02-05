#!/usr/bin/python3
"""
A module that defines a class MyList that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public methods:
        print_sorted(self): Prints the list in ascending order.

    Usage:
        my_list = MyList()
        my_list.append(1)
        my_list.append(4)
        my_list.append(2)
        my_list.append(3)
        my_list.append(5)
        print(my_list)
        my_list.print_sorted()
        print(my_list)
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Args:
            None

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
