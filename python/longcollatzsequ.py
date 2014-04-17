# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:22:47 2013

@author: Sebastien
"""
import time
def collatz(x, count):
    count += 1
    if x == 1:
        return count
    if not x % 2:
        return collatz(x/2, count)
    else:
        return collatz(x*3 + 1, count)
t = time.time()
i = 1
large = 0
large_no = 0

for i in xrange(1,1000001):
    count = 1
    seq_len = collatz(i, count)
    if seq_len > large:
        large = seq_len
        large_no = i

print "the largest collatz sequence with starting number under 1 000 000 is", large
print "the starting number is", large_no
print "code took", time.time() - t, "s to complete"