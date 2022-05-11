import math
import sys

N, W, H = map(int, sys.stdin.readline().split())

temp = math.sqrt(W*W+H*H)

for i in range(N):
    if int(input()) <= temp:
        print("DA")
    else:
        print("NE")
