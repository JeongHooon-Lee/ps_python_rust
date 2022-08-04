import sys

N, K = map(int, sys.stdin.readline().split())

datas = [str(i) for i in range(1, N+1)]
res: list = []
flag = 0
while datas:
    flag += (K-1)
    flag %= len(datas)
    res.append(datas.pop(flag))
print("<", ", ".join(res), ">", sep='')
