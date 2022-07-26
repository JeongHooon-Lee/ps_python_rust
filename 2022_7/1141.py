import sys

N = int(input())
datas: list = []
res = 0

for i in range(N):
    datas.append(sys.stdin.readline().strip())
datas.sort(key=len)

for i in range(N):
    flag = 0
    for j in range(i+1, N):
        if datas[i] == datas[j][:len(datas[i])]:
            flag = 1
            break

    if not flag:
        res += 1
print(res)
