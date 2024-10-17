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
    num_of_h = 1

    for i in range(2, n + 1):
        if n % i == 0:
            operations += 2
            n //= i
            num_of_h *= i

    return operations
