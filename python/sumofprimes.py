# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:14:05 2013

@author: Sebastien
"""

import math
import time

def primesieve(limit):
    num_range = [True] * limit
    num_range[0] = num_range[1] = False
    
    for i, isprime in enumerate(num_range):
        if isprime:
            for n in range(i*i, limit, i):
                num_range[n] = False
    return num_range
                
start = time.time()
limit = 2000000
primes = primesieve(limit)
prime_sum = 0
for num, state in enumerate(primes):
    if state:
        prime_sum += num
print "sum of first ", str(limit), " primes is: ", prime_sum
end = time.time()


print "code took: ", end - start, " s"