# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:50:07 2013

@author: ysebastien
"""
def factor(x):
    factor = []
    test_no = 2
    while np.prod(factor) != x:
        if not x % test_no:
            factor.append(test_no)
        test_no += 1
    return factor

def isprime(num):
    for i in range(2, num):
        if not num % i:
            return False
        elif i == num - 1:
            return True

import numpy as np

x = 600851475143
factor = factor(x)
prime_factors = [fac for fac in factor if isprime(fac)]
print max(prime_factors)