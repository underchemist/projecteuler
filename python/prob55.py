#!/usr/bin/env python3.3
"""
projecteuler.net - Problem 55: Lychrel Numbers
"""


def convert_to_string(val):
    if isinstance(val, int):
        return str(val)
    elif isinstance(val, str):
        return val
    else:
        raise ValueError


def is_palindrome(n):
    """ check if string version of a number is a palindrome """
    num_str = convert_to_string(n)
    if num_str == num_str[::-1]:
        return True
    else:
        return False


def transform(n):
    """
    perform arithmetic of reversing input and summing the result with
    the input.
    """
    num_str = convert_to_string(n)
    n_reversed = int(num_str[::-1])
    return n + n_reversed


def is_lychrel(n):
    """
    find if n is a lychrel number based on several criteria. Since these
    numbers are theoretical, we assume:
    - all numbers (below 10000) are lychrel until proven otherwise.
    - if a palindrome is not generated in 50 iterations, it is a lychrel
      number.
    """
    iteration_count = 0
    while iteration_count <= 50:
        next_n = transform(n)
        if is_palindrome(next_n):
            return False
        else:
            n = next_n
        iteration_count += 1

    return True

if __name__ == "__main__":
    lychrel_count = 0

    for n in range(1, 10000):
        if is_lychrel(n):
            lychrel_count += 1

    print("there are", lychrel_count, "Lychrel numbers below 10000")
