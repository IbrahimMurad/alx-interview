#!/usr/bin/python3
""" In this module we define a function that
determines if a given data set represents a valid UTF-8 encoding.
"""
from typing import List


def num_of_bytes(n: int) -> int:
    """ returns true if n is a valid byte """
    if n >> 7:
        if ~(n >> 3) == 0b11110:
            return 4
        elif ~(n >> 4) == 0b1110:
            return 3
        elif ~(n >> 5) == 0b110:
            return 2
        else:
            return 0
    return 1


def validUTF8(data: List[int]) -> bool:
    """ return true if data represents a valid UTF-8 encoding """
    i = 0
    data_length = len(data)
    while i < data_length:
        points = num_of_bytes(data[i])
        if points == 0:
            return False
        for j in range(points - 1):
            if data[i + j + 1] >> 6 != 0b10:
                return False
        i += points
    return True
