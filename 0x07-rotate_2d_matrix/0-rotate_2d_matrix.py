#!/usr/bin/python3
"""
Rotate a 2D matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix by 90
    degrees clockwise
    """
    rotated = zip(*reversed(matrix))
    for idx, row in enumerate(rotated):
        matrix[idx] = list(row)
