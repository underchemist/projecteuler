#!/usr/bin/env python3.3


def prime(x):
    for y in range(3, int(x ** 0.5) + 1, 2):
        if not x % y:
            return False
    return True


L = 1000000000
side_length = 1
jump = 0
n = 1
p = 0
on_diag = 1

while n <= L:
    jump += 2
    for i in range(4):
        n += jump
        on_diag += 1

        if prime(n):
            p += 1

    side_length += 2

    if float(p) / float(on_diag) < 0.1:
        print("side length is", side_length)
        break
