#!/usr/bin/env python3.3

import esieve3


def concatenate(n, m):
    return int(''.join([str(n), str(m)]))


def concatenable(n, m):
    p1 = concatenate(n, m)
    p2 = concatenate(m, n)

    if p1 in primes_set and p2 in primes_set:
        return True
    else:
        return False

# def load_to_dict(work_primes):
#     for n in work_primes:
#         if

if __name__ == '__main__':
    primes_lst = esieve3.gen_primes(30000)
    primes_set = set(primes_lst)
    con_primes = {p: set() for p in primes_set}

    for a in primes_set:
        for b in (primes_set - set([a])):
            if concatenable(a, b):
                con_primes[a].add(b)
                con_primes[b].add(a)

    if
