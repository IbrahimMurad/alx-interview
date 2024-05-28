#!/usr/bin/python3
"""
This module defines a function that returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """ Generates a list of lists representing the Pascal's triangle of n.

    Args:
        n (int): the height of the Pascal's triangle.
    """

    if n <= 0:
        return []

    # setting the first row since it has no previous list
    pascal = [[1]]

    for i in range(1, n):
        # appending the first element in each row
        # since it does't really depend on the previous list
        pascal.append([1])

        pascal[i].extend([
            pascal[i - 1][j] + pascal[i - 1][j + 1] for j in range(0, i - 1)
            ])

        # appending the last element in each row similar to the first one
        pascal[i].append(1)

    return pascal
