import sys

N, M = map(int, sys.stdin.readline().split())
datas = list(map(int, sys.stdin.readline().split()))
res: list = []

datas.sort()


def solve(d):
    if d == M:
        print(*res)
        return
    for i in range(N):
        res.append(datas[i])
        solve(d+1)
        res.pop()


solve(0)
