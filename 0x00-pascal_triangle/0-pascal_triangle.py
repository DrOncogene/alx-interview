#!/usr/bin/python3
"""
implementation of Pascal's triangle
"""


def pascal_triangle(n: int):
    """
    creates a list of lists that
    represents a Pascal's triangle

    :param n: int
        number of rows to compute

    Returns: a list of list representing the
             rows of the triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]
    for _ in range(3, n + 1):
        last_row = triangle[-1]
        row = [1]
        for i in range(1, len(last_row)):
            row.append(last_row[i] + last_row[i - 1])
        row.append(1)
        triangle.append(row)

    return triangle
