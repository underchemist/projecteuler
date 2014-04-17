#!/usr/bin/env python3.3

from fractions import Fraction
import sys
sys.setrecursionlimit(10001)


def f(max_iter, i=0):
    if i == max_iter:
        return 1.0 / 2.0
    elif i == 0:
        return 1.0 + 1.0 / (2.0 + f(max_iter, i + 1))
    else:
        return 1.0 / (2.0 + f(max_iter, i + 1))
