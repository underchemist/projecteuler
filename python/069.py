#!/usr/bin/env python3


from esieve3 import gen_primes


def main():
    p = gen_primes(1000000)
    prod = 1
    for prime in p:
        if prod * prime > 1000000:
            break
        prod *= prime

    print(prod)


if __name__ == '__main__':
    main()
