import sys

N, K = map(int, sys.stdin.readline().split())

res = 0

while bin(N).count('1') > K:
    N = N + 1
    res += 1
print(res)
