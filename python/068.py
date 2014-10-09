#!/usr/bin/env python3

from itertools import permutations


def is_valid(s):
    if s.index(10) not in (3, 5, 7, 9):
        return False
    if s[0] > min((s[3], s[5], s[7], s[9])):
        return False
    if sum(s[:3]) != sum([s[3], s[2], s[4]]): return False
    if sum(s[:3]) != sum([s[5], s[4], s[6]]): return False
    if sum(s[:3]) != sum([s[7], s[6], s[8]]): return False
    if sum(s[:3]) != sum([s[9], s[8], s[1]]): return False
    return True


def main():
    result = 0
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    indices = [0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 1]
    for perm in permutations(s):
        if is_valid(perm):
            temp = [str(perm[i]) for i in indices]
            temp = int(''.join(temp))
            if temp > result:
                result = temp

    print(result)

if __name__ == '__main__':
    main()
