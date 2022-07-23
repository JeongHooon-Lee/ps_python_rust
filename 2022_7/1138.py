import sys

N = int(input())
datas = list(map(int, sys.stdin.readline().split()))
res = {i: -1 for i in range(N)}

for i in range(N):
    cnt = 0
    for j in range(N):
        if res[j] == -1 and cnt == datas[i]:
            res[j] = i+1
            cnt += 1
        elif res[j] == -1:
            cnt += 1
print(*res.values())
