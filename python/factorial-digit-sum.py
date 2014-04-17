# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:34:26 2013

@author: ysebmac
"""

def factorial(n):
    if n < 1:   # base case
        return 1
    else:
        return n*factorial(n-1)  # recursive call
        
n_str = str(factorial(100))
sum_digit = 0

for char in n_str:
    char_int = int(char)
    sum_digit += char_int
    
print sum_digit