#!/usr/bin/python3
""" Island Perimeter problem solving script
"""


def is_valid_grid(grid):
    """ chaecks if the passed 2D matrix is a valid grid """
    if type(grid) is not list:
        return False
    for row in grid:
        if type(row) is not list:
            return False
    grid_height = len(grid)
    if grid_height > 100:
        return False
    for row in grid:
        if len(row) > 100:
            return False
    for row in grid:
        for element in row:
            if element not in [0, 1]:
                return False
    if any(grid[0]) or any(grid[-1]):
        return False
    for row in grid:
        if row[0] or row[-1]:
            return False
    return True


def island_perimeter(grid):
    """ solves island perimeter problem

    Args:
        grid (list[list[int]]): a 2D array contains only 0's and 1's
        0 represents water and 1 represents land
    """
    if not is_valid_grid(grid):
        return 0
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                perimeter += 4
                if grid[i-1][j]:
                    perimeter -= 1
                if grid[i+1][j]:
                    perimeter -= 1
                if grid[i][j-1]:
                    perimeter -= 1
                if grid[i][j+1]:
                    perimeter -= 1
    return perimeter
