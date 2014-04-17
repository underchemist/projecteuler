#!/usr/bin/env python

import esieve

# ones signify fixed digits and zeros repeating digits
def gen5DigitsReplace():
    return [[1,0,0,0,1],
            [0,1,0,0,1],
            [0,0,1,0,1],
            [0,0,0,1,1]]
# ones signify fixed digits and zeros repeating digits
def gen6DigitsReplace():
    return [[1,1,0,0,0,1],
            [1,0,1,0,0,1],
            [1,0,0,1,0,1],
            [1,0,0,0,1,1],
            [0,1,1,0,0,1],
            [0,1,0,1,0,1],
            [0,1,0,0,1,1],
            [0,0,1,1,0,1],
            [0,0,1,0,1,1],
            [0,0,0,1,1,1]]

if __name__ == "__main__":
    primes = esieve.gen_primes(1000)
