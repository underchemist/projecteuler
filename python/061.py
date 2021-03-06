#!/usr/bin/env python3.4
"""
Project Euler Problem 61
========================

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
are all figurate (polygonal) numbers and are generated by the following
formulae:

Triangle     P[3,n]=n(n+1)/2    1, 3, 6, 10, 15, ...
Square       P[4,n]=n^2         1, 4, 9, 16, 25, ...
Pentagonal   P[5,n]=n(3n-1)/2   1, 5, 12, 22, 35, ...
Hexagonal    P[6,n]=n(2n-1)     1, 6, 15, 28, 45, ...
Heptagonal   P[7,n]=n(5n-3)/2   1, 7, 18, 34, 55, ...
Octagonal    P[8,n]=n(3n-2)     1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties.

 1. The set is cyclic, in that the last two digits of each number is the
    first two digits of the next number (including the last number with
    the first).
 2. Each polygonal type: triangle (P[3,127]=8128), square (P[4,91]=8281),
    and pentagonal (P[5,44]=2882), is represented by a different number in
    the set.
 3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for
which each polygonal type: triangle, square, pentagonal, hexagonal,
heptagonal, and octagonal, is represented by a different number in the
set.
"""
def triangle(n): return int((n*(n+1))/2)

def square(n): return int(n*n)

def pentagonal(n): return int((n*(3*n-1))/2)

def hexagonal(n): return int((n*(2*n-1)))

def heptagonal(n): return int((n*(5*n-3))/2)

def octagonal(n): return int((n*(3*n-2)))

def is_cycle(a, b): return str(a)[-2:] == str(b)[:2]

figurates = {
    3: filter(lambda n: n < 10000 and n >= 1000, map(triangle, range(1000))),
    4: filter(lambda n: n < 10000 and n >= 1000, map(square, range(1000))),
    5: filter(lambda n: n < 10000 and n >= 1000, map(pentagonal, range(1000))),
    6: filter(lambda n: n < 10000 and n >= 1000, map(hexagonal, range(1000))),
    7: filter(lambda n: n < 10000 and n >= 1000, map(heptagonal, range(1000))),
    8: filter(lambda n: n < 10000 and n >= 1000, map(octagonal, range(1000)))
}

if __name__=='__main__':
    # generate all polygonal numbers
    numbers = [(key, value) for key in figurates.keys() for value in figurates[key]]

    for k1, v1 in numbers:
        for k2, v2 in [(k, v) for k, v in numbers if k not in [k1] and is_cycle(v1, v)]:
            for k3, v3 in [(k, v) for k, v in numbers if k not in [k1, k2] and is_cycle(v2, v)]:
                for k4, v4 in [(k, v) for k, v in numbers if not k in [k1, k2, k3] and is_cycle(v3, v)]:
                    for k5, v5 in [(k, v) for k, v in numbers if not k in [k1, k2, k3, k4] and is_cycle(v4, v)]:
                        for k6, v6 in [(k, v) for k, v in numbers if not k in [k1, k2, k3, k4, k5] and is_cycle(v5, v)]:
                            if is_cycle(v6, v1):
                                print(sum([v1, v2, v3, v4, v5, v6]))
                                
