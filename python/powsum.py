# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:48:31 2013

@author: ysebastien
"""
def numwordlen(num):
    numword = ""
    if len(num) == 4:
#        for j in xrange(len(num)):
        numword += "onethousand"
#            if j == 0:
#                numword += sindig[int(num[j])]
#                numword += thousand
#            if j == 1:
#                numword += sindig[int(num[j])]
#                numword += hund
#            if j == 2 and int(num[j]) > 1:
#                numword += "and"
#                numword += tens[int(num[j])]
#            if j == 2 and int(num[j]) < 2:
#                numword += "and"
#                if int(num[j]):
#                    numword += teens[int(num[j+1])]
#                else:
#                    numword += sindig[int(num[j+1])]
#            if j == 3 and int(num[j-1]) > 1 and int(num[j]) != 0:
#                numword += sindig[int(num[j])]
    if len(num) == 3:
        for k in xrange(len(num)):
            if k == 0:
                numword += sindig[int(num[k])]
                numword += hund
            if k == 1 and int(num[k]) > 1:
                numword += "and"
                numword += tens[int(num[k])]
            if k == 1 and int(num[k]) < 2:
                if int(num[k]) and int(num[k+1]): 
                    numword += "and"
                if not int(num[k]) and int(num[k+1]):
                    numword += "and"
                if int(num[k]) == 1 and not int(num[k+1]):
                    numword += "and"
                if int(num[k]):
                    numword += teens[int(num[k+1])]
                else:
                    numword += sindig[int(num[k+1])]
            if k == 2 and int(num[k-1]) > 1:
                numword += sindig[int(num[k])]
    if len(num) == 2:
        for l in xrange(len(num)):
            if l == 0 and int(num[l]) > 1:
                numword += tens[int(num[l])]
            if l == 1 and int(num[l-1]) < 2:
#                if int(num[l]):
                numword += teens[int(num[l])]
#                else:
#                    numword += sindig[int(num[l])]
            if l == 1 and int(num[l-1]) > 1 and int(num[l]) != 0:
                numword += sindig[int(num[l])]
    if len(num) == 1:
        numword += sindig[int(num[0])]
    return numword

import time
t = time.time()

sindig = ["","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["", "ten", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hund = "hundred"
thousand = "thousand"

s = 0
for i in xrange(1,1001):
    num = str(i)
    s += len(numwordlen(num))
print s
print "solution found in", time.time() - t, "s"