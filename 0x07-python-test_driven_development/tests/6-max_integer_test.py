#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """Unit tests for the max_integer function.

    These tests cover various scenarios:
    - Lists with integers.
    - Lists with floats.
    - Lists with negative floats and integers.
    - Empty lists.
    - Lists with single elements.

    Attributes:
        max_integer (function): The max_integer function to be tested.
    """

    def test_max_int_with_integers(self):
        """Test max_integer with lists containing only integers.

        Examples:
            - max_integer([1, 2, 3]) should return 3.
            - max_integer([5, 4, 3, 1]) should return 5.
            - max_integer([0, 0, 0]) should return 0.
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([5, 4, 3, 1]), 5)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_max_int_with_floats(self):
        """Test max_integer with lists containing floats.

        Examples:
            - max_integer([-5.0, -50, 0]) should return 0.
            - max_integer([0.9, 0.995, 0.0995]) should return 0.995.
        """
        self.assertEqual(max_integer([-5.0, -50, 0]), 0)
        self.assertEqual(max_integer([0.9, 0.995, 0.0995]), 0.995)

    def test_max_int_with_single_element(self):
        """Test max_integer with lists containing a single element.

        Examples:
            - max_integer([1]) should return 1.
        """
        self.assertEqual(max_integer([1]), 1)

    def test_max_int_with_empty_list(self):
        """Test max_integer with an empty list.

        Examples:
            - max_integer([]) should return None.
        """
        self.assertIsNone(max_integer([]))

    def test_max_int_with_no_arguments(self):
        """Test max_integer with no arguments.

        Examples:
            - max_integer() should return None.
        """
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
