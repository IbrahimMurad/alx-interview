#!/usr/bin/python3
""" This module defines a function that calculates
the fewest number of operations needed
to result in exactly n H characters in the file
It also defines all the required function to solve the problem.
"""
from typing import List, Optional


def minOperations(n: int) -> int:
    """ returns the minimum number of operations
    needed to result in exactly n H characters in the file """

    if n < 2:
        return 0
    divisor = 2
    operations = 0
    while n > 1:
        while n % divisor == 0:
            n = n / divisor
            operations += divisor
        divisor += 1
    return operations
