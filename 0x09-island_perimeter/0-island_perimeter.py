#!/usr/bin/python3
"""
calculating the perimeter of an island
"""
import itertools


def island_perimeter(grid: list[list[int]]):
    """finds the perimeter of an island
    represented by a grid (list of list)

    :param grid: list of list of 0s and 1s
    """

    perimeter = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                perimeter += water_neighbors(grid, (i, j))

    return perimeter


def water_neighbors(grid, pos):
    """
    """
    i, j = pos
    dim = len(grid), len(grid[0])
    neighbors = 0

    if i == 0 or grid[i - 1][j] == 0:
        neighbors += 1
    if i == dim[0] - 1 or grid[i + 1][j] == 0:
        neighbors += 1
    if j == 0 or grid[i][j - 1] == 0:
        neighbors += 1
    if j == dim[1] - 1 or grid[i][j + 1] == 0:
        neighbors += 1

    return neighbors
