#!/usr/bin/python3
"""
Module for solving lockboxes

"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    
    """
    unlocked = set([0])
    queue = [0]  # A queue to process boxes, starting with box 0

    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if key not in unlocked and key < len(boxes):  # Key is a valid box index that hasn't been unlocked
                unlocked.add(key)
                queue.append(key)
    
    return len(unlocked) == len(boxes)
