#!/usr/bin/env python


with open('p067_triangle.txt', 'r') as f:
    t = np.genfromtxt(f, dtype='int')


for i, j in [(k, l) for k in range(len(t)-2, -1, -1) for l in range(k+1)]:
    t[(i, j)] += max(t[(i+1, j)], t[(i+1, j+1)])

print(t[(0, 0)])
