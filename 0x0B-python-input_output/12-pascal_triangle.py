#!/usr/bin/python3
"""
This module defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: A list of lists representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[i - 1] + prev_row[i])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
