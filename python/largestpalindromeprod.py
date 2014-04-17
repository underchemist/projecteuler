# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:31:58 2013

@author: ysebastien
"""

def ispal(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] != num_str[len(num_str)-i-1]:
            return False
        elif i > len(num_str)/2:
            return True

palprod = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if ispal(i*j):
            palprod.append(i*j)
print max(palprod)