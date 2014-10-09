#!/usr/bin/env python3

EPS = 1e-10  # error limit
MAX = 134217728


def is_nth_root(a, n):
    # find if a is a perfect nth root, approximately ...
    return abs(int(round(a**(1/n))) - a**(1/n)) < EPS


def test(n, m):
    for i in range(n, m):
        key = is_nth_root(i, len(str(i)))
        if key:
            print(str(i))


def main():
    count = 0
    for x in range(10, MAX):
        if is_nth_root(x, len(str(x))):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
