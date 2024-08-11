#!/usr/bin/python3
""" Module that determines if all the boxes can be opened. """


def canUnlockAll(boxes):
    """Function that determines if all the boxes can be opened."""
    if len(boxes) == 0:
        return False

    unlocked = set([0])  # boxes that are unlocked
    to_check = [0]  # boxes that we still need to check

    while to_check:
        current = to_check.pop(0)
        for key in boxes[current]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                to_check.append(key)

    return len(unlocked) == len(boxes)
