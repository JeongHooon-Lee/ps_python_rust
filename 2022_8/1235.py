import sys

N = int(input())
datas: list = []
for i in range(N):
    data = sys.stdin.readline().strip()
    datas.append(data[::-1])

for i in range(1, len(datas[0])+1):
    temp: list = []
    for j in range(N):
        temp.append(datas[j][:i])
    temp = set(temp)
    if len(temp) == N:
        print(i)
        break
    else:
        continue
