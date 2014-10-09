#!/usr/bin/env python3

from math import floor


def gen_cf_period(r):
    """generate periodic continued fraction notation"""
    m = 0
    d = 1
    a = a0 = floor(r)
    period = 0

    while a != 2*a0:
        m = round(d*a - m)
        d = round((r*r - m*m)/d)
        a = round(floor((a0 + m)/d))
        period += 1
    return period


def main():
    count = 0
    for i in range(10000):
        if i == floor(i**0.5)**2:
            continue
        if gen_cf_period(i**0.5) % 2:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
