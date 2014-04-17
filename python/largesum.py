# -*- coding: utf-8 -*-
"""
Created on Mon May 13 23:12:36 2013

@author: ysebastien
"""

import os
import time
import numpy as np

t = time.clock()
num = []
f = open(os.path.expanduser("~/Dropbox/Code/Python/projecteuler.net/largesumdata.txt"), "r")
num = np.genfromtxt(f, dtype="str")
f.close()

s = 0
for item in num:
    s += int(item)
s_srt = str(s)

print s_srt[:10]
print "code took", time.clock() - t, "s to complete"
