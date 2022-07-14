import sys

N, M = map(int, sys.stdin.readline().split())
datas: list = []
res = 0
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    if B != 0 and A/B < 6:
        datas.append((A/6, A, 6))
    datas.append((B, B, 1))
datas.sort()

if datas[0][2] == 1:
    print(datas[0][0]*N)
else:
    res = (N // 6) * datas[0][1]
    N = N % 6
    tmp = 1
    while True:
        if datas[tmp][2] == 1:
            break
        tmp += 1
    if datas[tmp][0] * N < datas[0][1]:
        res += datas[tmp][0] * N
    else:
        res += datas[0][1]
    print(res)
