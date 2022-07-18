import sys

N, M = map(int, sys.stdin.readline().split())
A: list = []
B: list = []
res = 0
flag = 1
for i in range(N):
    temp = list(map(int, list("".join(sys.stdin.readline().strip()))))
    A.append(temp)
for i in range(N):
    temp = list(map(int, list("".join(sys.stdin.readline().strip()))))
    B.append(temp)


def solutions(y, x):
    for i in range(y, y+3):
        for j in range(x, x+3):
            B[i][j] = 1 - B[i][j]


for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            solutions(i, j)
            res += 1
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            flag = 0
            break
if not flag:
    print(-1)
else:
    print(res)
