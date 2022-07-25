import sys

N, T, P = map(int, sys.stdin.readline().split())
datas = list(map(int, sys.stdin.readline().split()))

res = 0
if N == 0:
    print(1)
elif N == P and datas[-1] >= T:
    print(-1)
else:
    res = N+1
    for i in range(N):
        if datas[i] <= T:
            res = i+1
            break
    print(res)
