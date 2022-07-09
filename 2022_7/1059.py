import sys

L = int(input())
datas = list(map(int, sys.stdin.readline().split()))
N = int(input())

datas.sort()
res = 0
for i in range(L):
    if N < datas[i]:
        left = datas[i-1]
        right = datas[i]
        break

if N < datas[0]:
    for i in range(1, N+1):
        for j in range(N, datas[0]):
            if i == j:
                continue
            else:
                res += 1

else:
    for i in range(left+1, N+1):
        for j in range(N, right):
            if i == j:
                continue
            res += 1

print(res)
