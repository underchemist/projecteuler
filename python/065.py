#!/usr/bin/env python3

from fractions import Fraction


def step(s, count, p):
    if not count:
        return Fraction(s)
    return step(Fraction(p[count-1] + 1/s), count-1, p)


def main():
    # generate period of e
    p = [2]
    p.extend([i for k in range(1, 100) for i in (1, 2*k, 1)])

    n = step(p[100-1], 100-1, p)
    a = str(n.numerator)
    print(sum([int(v) for v in a]))

if __name__ == '__main__':
    main()
