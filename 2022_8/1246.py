import sys

N, M = map(int, sys.stdin.readline().split())
datas: list = []
for i in range(M):
    datas.append(int(input()))

datas.sort()
res = [(datas[i], datas[i]*min(M-i, N)) for i in range(M)]
res.sort(key=lambda x: x[1], reverse=True)
print(*res[0])
