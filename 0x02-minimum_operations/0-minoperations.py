#!/usr/bin/python3
"""0-minoperations module"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed
    to achieve exactly n 'H' characters

    Parameters:
    n (int): The target number of 'H' characters to achieve.

    Returns:
    int: The minimum number of operations required to reach exactly n 'H'
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
