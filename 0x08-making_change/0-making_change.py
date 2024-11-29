#!/usr/bin/python3
"""
Make change Module
"""


def makeChange(coins, amount):
    """
    Calculate the minimum number of coins needed
    to make a given amount of money.
    """
    if amount < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if amount == 0:
            break
        num = amount // coin
        amount -= num * coin
        count += num
    return count if amount == 0 else -1
