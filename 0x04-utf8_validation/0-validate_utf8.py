#!/usr/bin/python3
""" In this module we define a function that
determines if a given data set represents a valid UTF-8 encoding.
"""
from typing import List


def significant_8(sequence: List[int]) -> List[int]:
    """ returns the same list but with only the first 8 significant digits """
    return [n & 0b11111111 for n in sequence]

def num_of_bytes(n: int) -> int:
    """ returns true if n is a valid byte """
    if n >> 7:
        if (n >> 3) == 0b11110:
            return 4
        elif (n >> 4) == 0b1110:
            return 3
        elif (n >> 5) == 0b110:
            return 2
        else:
            return 0
    return 1


def check_seq_bytes(continuation_bytes: List[int]) -> bool:
    """ Checks the continuation_bytes """
    for i in continuation_bytes:
        if i >> 6 != 0b10:
            return False
    return True


def overlong(sequence: List[int]) -> bool:
    """ checks if the sequence is overlong """
    bytes_num = len(sequence)
    encoded_value = sequence[0] & (0xFF >> (bytes_num + 1))
    min_value = [0, 0x7f, 0x7ff, 0xffff]
    for i in range(1, bytes_num):
        encoded_value <<= 6
        encoded_value |= (sequence[i] & 0b00111111)
    if encoded_value <= min_value[bytes_num - 1]:
        return True
    return False


def validUTF8(data: List[int]) -> bool:
    """ return true if data represents a valid UTF-8 encoding """
    data = significant_8(data)
    i = 0
    data_length = len(data)
    while i < data_length:
        points = num_of_bytes(data[i])
        if points == 0 or (i + points) > data_length:
            return False
        if points > 1:
            if not check_seq_bytes(data[i + 1:i + points]):
                return False
            if overlong(data[i:i + points]):
                return False
        i += points
    return True
