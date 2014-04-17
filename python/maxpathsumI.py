# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:22:06 2013

@author: ysebastien
"""

import os
import numpy as np
import time

f = open(os.path.expanduser("~/Dropbox/Code/projecteuler/python/maxpathsumIdata.txt"), "r")
t = np.genfromtxt(f, dtype="int")
f.close()

start = time.time()

for i,j in [(k,l) for k in range(len(t)-2,-1,-1) for l in range(k+1)]:
    t[(i,j)] += max(t[(i+1,j)], t[(i+1,j+1)])

print t[(0,0)]
print "solution found in", time.time() - start, "s"
