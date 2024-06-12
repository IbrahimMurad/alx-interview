#!/usr/bin/python3
""" This module defines a function that calculates
the fewest number of operations needed
to result in exactly n H characters in the file
It also defines all the required function to solve the problem.
"""


def minOperations(n: int) -> int:
    """ returns the minimum number of operations
    needed to result in exactly n H characters in the file """

    primes = [
        i for i in range(2, n + 1)
        if all([i % j != 0 for j in range(2, i)])
    ]
    if n < 2:
        return 0
    for prime in primes:
        if n % prime == 0:
            return prime + minOperations(int(n / prime))
    return 0
