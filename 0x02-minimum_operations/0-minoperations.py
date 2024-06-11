#!/usr/bin/python3
""" This module defines a function that calculates the fewest number of operations needed to result in exactly n H characters in the file
It also defines all the required function to solve the problem.
"""


def primes(n: int) -> list[int]:
    """ returns a list of all the prime numbers up to n 
    except for 2 """
    return [i for i in range(3, n + 1) if all([i % j != 0 for j in range(2, i)])]


def minOperations(n: int) -> int:
    """ returns the minimum number of operations
    needed to result in exactly n H characters in the file """

    if n < 2:
        return 0
    if n == 2:
        return 2
    if n % 2 == 0:
        return 2 + minOperations(int(n / 2))
    for i in primes(n):
        if n == i:
            return i
        if n % i == 0:
            return i + minOperations(int(n / i))
    return 0
