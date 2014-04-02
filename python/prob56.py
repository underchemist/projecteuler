#!/usr/bin/env python3.3


def convert_to_string(val):
    if isinstance(val, int):
        return str(val)
    elif isinstance(val, str):
        return val
    else:
        raise ValueError


def digital_sum(n):
    """ find sum of the digits of a number """
    n_lst = list(convert_to_string(n))
    return sum([int(i) for i in n_lst])

if __name__ == "__main__":
    max_digital_sum = 0
    for a in range(2,100):
        for b in range(2,100):
            result = digital_sum(a**b)
            if max_digital_sum < result:
                max_digital_sum = result

    print("the largest digital sum for numbers of the form a^b is", max_digital_sum)
