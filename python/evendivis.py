# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:16:44 2013

@author: ysebastien
"""

def isdiv(x, test):
    rel_num = [7,9,11,12,13,14,15,16,17,18,19]
    ind = rel_num.index(test)
    if test == 7:
        return True
    if not x % test:
        return isdiv(x, rel_num[ind-1])
    else: return False
#    for i in set(rel_num):
#        if not x % i:
#            count += 1
#    if count == len(set(rel_num)):
#        return True
#    else: return False

import time
start = time.time()
check = 20
while True:
    if isdiv(check, 19):
        break
    check += 20
print check
end  = time.time()

print end - start

