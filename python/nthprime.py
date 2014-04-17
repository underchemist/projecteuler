# -*- coding: utf-8 -*-
"""
Created on Mon May 13 08:57:24 2013

@author: ysebastien
"""

def isprime(x):
    if x < 9:
        for i in range(2, x):
            if not x % i:
                return False
    else:
        for j in range(2, int(math.floor(math.sqrt(x))) + 1):
            if not x % j:
                return False
    return True

import time
import math

start = time.time()
primes = [2]
num = 3
n = 1

while n!= 10001:
    if isprime(num):
        n += 1
    num += 2
print "10 0001th prime number is: ", num
end = time.time()

print "time: ", end - start, " s"
