# -*- coding: utf-8 -*-
"""
projecteuler.net problem 21 - Amicable Numbers
@author: underchemist
@date: 2013-09-13
@problem:

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

def pdiv_sum(n):
    sum = 1
    for i in range(2,n):
        if n % i == 0:
            sum += i
    return sum

def gen_amic():
    amic_pot = []
    
    for j in range(1,high):
        num = pdiv_sum(j)
        if num < high:
            amic_pot.append(num)
    return amic_pot

high = 10000
amicable_nums = []
for l in range(2,high):
    k = pdiv_sum(l)
    m = pdiv_sum(k)
    if m == l and k < high and m < high and k != m:
        amicable_nums.append(l)
print sum(amicable_nums)