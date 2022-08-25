import sys

N = int(input())
datas: list = []
for i in range(N):
    datas.append(list(map(int, sys.stdin.readline().split())))
datas.sort(key=lambda x: (x[1], x[0]))
max_res = datas[0][1]-datas[0][0]
flag = 1
res = 0
for i in range(max_res, -1, -1):
    now = i + datas[0][0]
    flag = 1
    for S, T in datas[1:]:
        now += S
        if now > T:
            flag = 0
            break
    if flag:
        res = i
        break
if not flag or max_res < 0:
    print(-1)
else:
    print(res)
