#!/usr/bin/python3
def minOperations(n):
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
