# -*- coding: utf-8 -*-
"""
Created on Mon May 13 20:29:58 2013

@author: ysebastien
"""

def primefactors(x):
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
        else:
            loop+=1
    return factorlist

import time
start = time.time()
tri = 1
i = 1
while True:
    pfactors = primefactors(tri)
    exp = []
    s = 0
    for j in pfactors:
        if j != s:
            s = j
            exp.append(pfactors.count(j))
    p = 1
    for k in exp:
        p *= k+1
    if p >= 500:
        break
    else:
        i += 1
        tri = int((i*(i+1))/2)
print tri

end = time.time()
print "that took:", end-start,"s to complete"