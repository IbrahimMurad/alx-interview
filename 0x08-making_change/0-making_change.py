#!/usr/bin/python3
""" Making Change module
"""


def makeChange(coins: list[int], total: int) -> int:
    """ calculates the fewest number of coins needed
    to meet a given amount total using the coins provided in coins list

    Args:
        coins (list[int]): a list of the values of the coins in your possession
        total (_type_): the given amount
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin
    return count if total == 0 else -1
