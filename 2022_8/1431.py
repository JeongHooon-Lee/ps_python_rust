import sys

datas: list = []

for i in range(int(input())):
    data = sys.stdin.readline().strip()
    temp = 0
    for j in data:
        if j.isdigit():
            temp += int(j)
    datas.append((len(data), temp, data))
datas.sort(key=lambda x: (x[0], x[1], x[2]))
for i in datas:
    print(i[2])
