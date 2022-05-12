import math
import sys

W, H, X, Y, P = map(int, sys.stdin.readline().split())
data: list = []
for i in range(P):
    data.append(list(map(int, sys.stdin.readline().split())))


def distance(x1, y1):
    x2 = X
    y2 = Y+H/2
    x3 = X+W
    y3 = Y+H/2
    temp = math.sqrt((x2-x1)**2+(y2-y1)**2)
    temp2 = math.sqrt((x3-x1)**2+(y3-y1)**2)
    if temp <= H/2 or temp2 <= H/2 or (X <= x1 <= X+W and Y <= y1 <= Y+H):
        return 1
    return 0


res = 0
for pos in data:
    if distance(pos[0], pos[1]):
        res += 1

print(res)
