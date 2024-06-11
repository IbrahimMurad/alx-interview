#!/usr/bin/python3
""" This module defines a function that calculates
the fewest number of operations needed
to result in exactly n H characters in the file
It also defines all the required function to solve the problem.
"""


def minOperations(n: int, primes: list[int] = []) -> int:
    """ returns the minimum number of operations
    needed to result in exactly n H characters in the file """

    if n < 2:
        return 0
    if not primes:
        primes = [
            i for i in range(2, n + 1)
            if all([i % j != 0 for j in range(2, i)])
            ]
    for prime in primes:
        if n % prime == 0:
            return prime + minOperations(int(n / prime), primes)
    return 0
