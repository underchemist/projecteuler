#!/usr/bin/env python3
"""
Created on Tue May 14 23:22:06 2013

@author: ysebastien
"""


def recSumAtRow(rowData, rowNum):
    # iterate over the given row
    for i in range(len(rowData[rowNum])):
        # add the largest of the values below-left or below-right
        rowData[rowNum][i] += max([rowData[rowNum+1][i], rowData[rowNum+1][i+1]])
    # base case
    if len(rowData[rowNum]) == 1:
        return rowData[rowNum][0]
    # recursive case
    else:
        return recSumAtRow(rowData, rowNum-1)


t = []
with open('triangle.txt') as f:
    for line in f:
        t.append([int(i) for i in line.rstrip('\n').split(" ")])

result = recSumAtRow(t, len(t)-2)  # start at second to last row

print(result)
