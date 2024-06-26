#!/usr/bin/python3
"""
This module solves the problem of minimum operations

"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file

    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    while factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
