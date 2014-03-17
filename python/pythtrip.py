# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:46:25 2013

@author: Sebastien
"""

def istrip(a, b, c):
    if not a**2 + b**2 - c**2:
        return True
    else:
        return False


for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            if i+j+k == 1000:
                if istrip(i, j, k):
                    print i*j*k
                    