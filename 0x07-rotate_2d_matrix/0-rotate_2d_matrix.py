#!/usr/bin/python3
""" This module defines a function that rotates a 2D-Matrix 90 degree clockwise
"""


def rotate_2d_matrix(matrix):
    """ rotates matrix 90 degree clockwise in place
    matrix is a list of lists """
    matrix.reverse()
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
