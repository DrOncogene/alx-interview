#!/usr/bin/python3
"""
validate utf-8 encoding
"""
import re


def binary(num):
    """
    returns the complete binary repr
    of an integer padded when necessary
    """
    res = bin(num)[2:]
    rem = len(res) % 4
    if rem == 0:
        return res

    diff = abs(rem - 4)
    return f"{'0' * diff}{res}"



def validUTF8(data):
    """
    validates utf-8 encoding
    """
    multi_byte = re.compile(r'(11+)0\d*')
    bin_data = [binary(num)[-8:] for num in data]

    next_byte = 0
    for idx, num in enumerate(bin_data):
        if idx != next_byte:
            continue
        if num.startswith('0'):
            next_byte = idx + 1
            continue
        if num.startswith('10'):
            return False

        res = multi_byte.findall(num)
        num_bytes = len(res[0])
        for i in range(1, num_bytes):
            if not bin_data[idx + i].startswith('10'):
                return False
        next_byte = idx + num_bytes + 1

    return True
