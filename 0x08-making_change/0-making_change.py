#!/usr/bin/python3
"""
determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """makes total from a collection of coins"""
    if total <= 0:
        return 0

    return make_change(coins, total, 0)
    

def make_change(coins, total, n_coins):
    """
    recursively finds the fewest number
    of coins from coins to make total
    """

    if total <= 0:
        return n_coins

    coins = sorted([c for c in coins if c <= total])
    if len(coins) == 0:
        return -1

    rem = total % coins[-1]
    n_coins += int(total / coins[-1])

    return make_change(coins[:-1], rem, n_coins)
