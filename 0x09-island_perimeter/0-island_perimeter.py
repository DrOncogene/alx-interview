#!/usr/bin/python3
"""
calculating the perimeter of an island
"""


def island_perimeter(grid):
    """finds the perimeter of an island
    represented by a grid (list of list)

    :param grid: list of list of 0s and 1s
    """

    size = 0
    for row in grid:
        size = longest_stretch(row, size)

    for col in zip(*grid):
        size = longest_stretch(col, size)

    return size * 4


def longest_stretch(row, size):
    """
    finds the longest stretch of 1s from a list
    and compare it to longest from other lists in the grid

    :param row: list of 0s and 1s
    :param size: longest stretch from preceeding lists
    """

    stretches = []
    longest = 0
    for num in row:
        if num == 1:
            longest += 1
        elif num == 0 and longest > 0:
            stretches.append(longest)
            longest = 0

    if len(stretches) == 0:
        return size

    return size if max(stretches) < size else max(stretches)

