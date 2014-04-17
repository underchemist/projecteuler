# -*- coding: utf-8 -*-
"""
projecteuler.net problem 22 - Names
@author: underchemist
@date: 2013-09-13
"""

def name_val(name):
    val = 0
    for char in name:
        val += letter_val[char]
    return val


import csv

letter_val = dict(A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,I=9,J=10,K=11,L=12,M=13,N=14,O=15,P=16,Q=17,R=18,S=19,T=20,U=21,V=22,W=23,X=24,Y=25,Z=26)
f = open("/home/ysebastien/Dropbox/Python/projecteuler.net/names.txt", "r")
csv_obj = csv.reader(f, delimiter=",", quotechar="\"")
for names in csv_obj:
    print "got names"
f.close()

sum = 0
names_sorted = sorted(names)
for ind, name in enumerate(names_sorted):
    sum += (ind + 1)*name_val(name)
    
print sum