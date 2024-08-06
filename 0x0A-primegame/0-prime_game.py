#!/usr/bin/python3
""" prime game solver
"""

primes = [2, 3]


def primeNumbers(n):
    """ returns a list of prime numbers up to n """
    if n == primes[-1]:
        return primes
    elif n < primes[-1]:
        for prime in primes:
            if n < prime:
                return primes[0:primes.index(prime)]
    i = primes[-1] + 2
    isPrime = False
    while i <= n:
        for prime in primes:
            if i % prime == 0:
                isPrime = False
                break
            else:
                isPrime = True
        if isPrime:
            primes.append(i)
        i += 2
    return primes


def turnWinner(number):
    """ determines the winner of the current turn """
    return len(primeNumbers(number)) % 2


def isWinner(x, nums):
    """ The prime game """
    MaraiWins = 0
    BenWins = 0
    for i in range(x):
        if turnWinner(nums[i]):
            MaraiWins += 1
        else:
            BenWins +=1
    if MaraiWins > BenWins:
        return 'Maria'
    elif BenWins > MaraiWins:
        return 'Ben'
    return None
