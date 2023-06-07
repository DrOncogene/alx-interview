#!/usr/bin/python3
"""
calculating the perimeter of an island
"""


def island_perimeter(grid):
    """finds the perimeter of an island
    represented by a grid (list of list)

    :param grid: list of list of 0s and 1s
    """

    perimeter = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                perimeter += edges(grid, (i, j))

    return perimeter


def edges(grid, cell):
    """
    finds the apropriate perimeter of each cell by
    checking for water cells or edges and adding 1 to
    the perimeter

    :param grid: the grid
    :param cell: cell coordinates (i, j)
    """
    i, j = cell
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
