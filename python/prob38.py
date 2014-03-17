#!/usr/bin/env python

def findmatch(P):
    for i,char in enumerate(P):
        tempchar = char
        tempind = i
        for j in P[tempind+1:]:
            if tempchar == j:
                return True

    return False

def findnextint(I):
    if findmatch(str(I)):
        if not I % 100:
            return findnextint(I+(I/100) + 1)
        else:
            return findnextint(int(I+1))
    else:
        return int(I)

myint = 1
maxsize = 9
endsignal = 0
maxprod = 0

while not endsignal:
    prod = ''
    for i in range(1,maxsize+1):
        if len(str(myint)) > 9:
            endsignal = 1
            break
        prod += str(myint*i)
        if findmatch(prod) or len(prod) > 9:
            break
        if int(prod) > maxprod:
            maxprod = int(prod)
    print myint, ": ", str(maxprod)
    myint = findnextint(myint+1)
print maxprod



