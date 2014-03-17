# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:12:05 2013

@author: Sebastien
"""

import numpy as np
import time

t = time.time()
gridsize = 41
grid = np.ones((gridsize,)*2, dtype="int")

for i in xrange(gridsize-2,-1,-1):
    for j in xrange(gridsize-2,-1,-1):
        grid[(i,j)] = grid[i+1,j] + grid[i,j+1]

print "there are", grid[(0,0)], "possible paths in a 20x20 grid"
print "solution took", time.time() - t, "s to complete"
