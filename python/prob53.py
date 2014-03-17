#!/usr/bin/env python

from math import factorial, ceil

def choose(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

if __name__ == '__main__':
    upperLimit = 1000000
    count = 0
    for n in range(1,101):
        subLimit = int(ceil(n/2))
        for r in range(1, subLimit):
            if choose(n, r) >= upperLimit:
                count += (subLimit - r)*2+1
                if n % 2:
                    count += 1
                break
    print "there are ", count, "values of nCr above 1000000"