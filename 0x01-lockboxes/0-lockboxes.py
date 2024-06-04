#!/usr/bin/python3
""" This module defines a function that solves the lockboxes problem
in which we have a collection of boxes,
and each box has zero or more keys to other boxes (or itself)
All the boxes are closed except for the first one,
and the goal is to get all the keys for all the boxes to be able to unlock them
"""


def canUnlockAll(boxes):
    """ Solves the lockboxes problem

    Args:
        boxes (list[list[int]]): list of lists of ints
        describing a collection of boxes (lists) that have keys (ints)

    Returns:
        boolean: True if all the boxes can be unlocked
        or False if one or more boxes can not be unlocked
    """
    required_keys = set(range(1, len(boxes)))
    locks = {
        "unlocked": {0},
        "locked": required_keys.copy(),
        'checked': set()
        }
    tikked = True
    while tikked:
        locked = locks["locked"].copy()
        unlocked = locks["unlocked"].copy()
        checked = locks["checked"].copy()
        if not locked:
            return True
        for key in unlocked - checked:
            locks["unlocked"].update(boxes[key])
            locks["unlocked"].intersection_update(required_keys)
            locks["locked"].difference_update(locks["unlocked"])
            locks["checked"].add(key)
        tikked = locked - locks["locked"] != set()
    return False
