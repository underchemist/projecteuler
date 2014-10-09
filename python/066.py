#!/usr/bin/env python3

from math import floor
from itertools import cycle


def period(r):
    """generate periodic continued fraction notation"""
    m = 0
    d = 1
    a = a0 = floor(r)
    p = []

    while a != 2*a0:
        m = round(d*a - m)
        d = round((r*r - m*m)/d)
        a = round(floor((a0 + m)/d))
        p.append(a)
    return (a0, p)


def update(hn, h1, h2, kn, k1, k2):
    """swap values"""
    return (hn, hn, h1, kn, kn, k1)


def convergents(D):
    """attempt at generator function"""
    h1 = k2 = 1
    h2 = k1 = hn = kn = 0
    a0, p = period(D)
    hn = int(a0*h1 + h2)
    kn = int(a0*k1 + k2)
    hn, h1, h2, kn, k1, k2 = update(hn, h1, h2, kn, k1, k2)
    yield (hn, kn)
    for a in cycle(p):
        hn = int(a)*int(h1) + int(h2)
        kn = int(a)*int(k1) + int(k2)
        yield (hn, kn)
        hn, h1, h2, kn, k1, k2 = update(hn, h1, h2, kn, k1, k2)


def main():
    min_solution = dict()
    for i in range(1, 1001):
        if i == floor(i**0.5)**2:
            continue
        for h, k in convergents(i**0.5):
            if h**2 - i*k**2 == 1:
                min_solution[i] = h
                break
    print(max(min_solution, key=min_solution.get))


if __name__ == '__main__':
    main()
