import sys
from math import sqrt

xa, ya, xb, yb, xc, yc = map(int, sys.stdin.readline().split())
distances = [[ya, xa], [yb, xb], [yc, xc]]
res_max = 0
res_min = 0
res: list = []


def gradient(a, b):
    return sqrt(((a[0]-b[0])**2 + (a[1] - b[1])**2))


for a, b in [[0, 1], [1, 2], [0, 2]]:
    res.append(gradient(distances[a], distances[b]))

if (xa-xb)*(yb-yc) == (xb-xc)*(ya-yb):
    print(-1)
else:
    print((max(res)-min(res)) * 2)
