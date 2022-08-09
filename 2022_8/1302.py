import sys

N = int(input())
datas: list = {}

for i in range(N):
    data = sys.stdin.readline().strip()
    try:
        datas[data] -= 1
    except:
        datas[data] = -1

temp = sorted([(data, datas[data])
              for data in datas.keys()], key=lambda x: (x[1], x[0]))
print(temp[0][0])
