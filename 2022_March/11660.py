import sys

N, M = map(int, sys.stdin.readline().split())
arr : list = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,N):
    for j in range(N):
        arr[i][j] = arr[i][j] + arr[i-1][j]

for i in range(M):
    res = 0
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    for j in range(y1-1,y2):
        res += arr[x2-1][j]
    if x1 >= 2:
        for j in range(y1-1,y2):
            res -= arr[x1-2][j]
    print(res)

#pypy