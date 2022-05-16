import sys

N, M = map(int, sys.stdin.readline().split())
datas = list(map(int, sys.stdin.readline().split()))
dp = [0]
res = 0

remainder = {i: 0 for i in range(M)}

for i in range(N):
    temp = (dp[-1]+datas[i]) % M
    dp.append(temp)
    remainder[temp] += 1
    if temp == 0:
        res += 1


def count(remainder: dict) -> int:
    global res

    for value in remainder.values():
        if value > 1:
            res += (value*(value-1))//2
    print(res)


count(remainder)
