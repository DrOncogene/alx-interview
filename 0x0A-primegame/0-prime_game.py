#!/usr/bin/python3
"""the prime game"""


def isWinner(x, nums):
    """determins the winner of the game after x rounds
    """
    if x <= 0:
        return None

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

    def play_round(turn, round_len, round_numbers):
        if round_len in memoize:
            update_score(memoize[round_len])
            return

        prime = get_prime(round_numbers)
        while prime:
            round_numbers = [num for num in round_numbers
                             if num % prime != 0]

            turn = 'm' if turn == 'b' else 'b'

            prime = get_prime(round_numbers)

        update_score('m' if turn == 'b' else 'b')
        memoize[round_len] = 'm' if turn == 'b' else 'b'

    for i in range(x):
        curr_round = nums[i]
        round_nums = [j + 1 for j in range(curr_round)]

        turn = 'm'
        play_round(turn, nums[i], round_nums)

    if scores['Ben'] == scores['Maria']:
        return None

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
    if num in [2, 3, 5, 7]:
        return True

    median = int(num / 2)
    for i in range(2, median + 1):
        if num % i == 0:
            return False

    return True
