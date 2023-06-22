#!/usr/bin/python3
"""the prime game"""


def isWinner(x, nums):
    """determins the winner of the game after x rounds
    """
    scores = {
        'Maria': 0,
        'Ben': 0
    }

    memoize = {}

    def update_score(turn):
        if turn == 'm':
            scores['Maria'] += 1
        else:
            scores['Ben'] += 1

    for i in range(x):
        round_nums = [j + 1 for j in range(nums[i])]
        turn = 'm'
        for idx, num in enumerate(round_nums.copy()):
            if num in memoize:
                update_score(memoize[num])
                break

            prime = get_prime(round_nums)
            if not prime:
                update_score(turn)
                memoize[num] = 'm' if turn == 'b' else 'b'
                print(memoize)
                break

            for num2 in round_nums:
                if num2 % prime == 0:
                    round_nums.pop(idx)

            if turn == 'm':
                turn = 'b'
    return ('Maria' if scores['Maria'] > scores['Ben']
            else 'Ben')


def get_prime(num_list):
    """finds the smallest prime number in a list
    """
    for num in num_list:
        if is_prime(num):
            return num
    else:
        return None


def is_prime(num):
    """determines whether a number is
    prime or not
    """
    if num == 1:
        return False

    median = int(num / 2)
    for i in range(1, median + 1):
        if num % i == 0:
            return False

    return True
