from re import L
import sys


def func(x,y):
    res = 0
    for i in range(M):
        res += A[x][i] * B[i][y]
    return res
A : list = []
B : list = []

N,M = map(int, sys.stdin.readline().split())
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

M,K = map(int, sys.stdin.readline().split())
for i in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))

array = [ [0]*K for _ in range(N) ]

for i in range(N):
    for j in range(K):
        array[i][j] += func(i,j)

for i in array:
    print(*i)
