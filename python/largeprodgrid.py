# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:33:05 2013

@author: ysebastien
"""

import numpy as np
import time
import os

def valid(index):
    vec = [True]*8 # number of possible product directions starting with up
    
    if index[0] < 3:
        vec[0] = False
    if index[0] < 3 or index[1] > 16:
        vec[1] = False
    if index[1] > 16:
        vec[2] = False
    if index[0] > 16 or index[1] > 16:
        vec[3] = False
    if index[0] > 16:
        vec[4] = False
    if index[0] > 16 or index[1] < 3:
        vec[5] = False
    if index[1] < 3:
        vec[6] = False
    if index[0] < 3 or index[1] < 3:
        vec[7] = False
    return vec
    
def direct(inp, index):
    if inp == 0:
        return (-1*index[0], 0*index[1])
    elif inp == 1:
        return (-1*index[0], 1*index[1])
    elif inp == 2:
        return (0*index[0], 1*index[1])
    elif inp == 3:
        return (1*index[0], 1*index[1])
    elif inp == 4:
        return (1*index[0], 0*index[1])
    elif inp == 5:
        return (1*index[0], -1*index[1])
    elif inp == 6:
        return (0*index[0], -1*index[1])
    elif inp == 7:
        return (-1*index[0], -1*index[1])

start = time.time()
f = open(os.path.expanduser("~/Dropbox/Python/Scripts/projecteuler.net/largeprodgrid_data.txt"), "r")
A = np.genfromtxt(f, dtype="int")
f.close()
l_prod = 0
for row, i in enumerate(A):
    for col, j in enumerate(i):
        vec = valid((row,col))
        for state_ind, state in enumerate(vec):
            if state:
                prod_list = [A[(row,col)]]
                for l in range(1,4):
                    (m, n) = direct(state_ind, (l,l))
                    prod_list.append(A[(row + m, col + n)])
                prod = np.prod(prod_list)
                if prod > l_prod:
                    l_prod = prod
print l_prod
                    
end = time.time()