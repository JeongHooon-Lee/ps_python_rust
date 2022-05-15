# pypy
# import sys

G = int(input())
P = int(input())
datas: list = []

docking = [i for i in range(G+1)]
res = 0


def find_parent(v):
    if v == docking[v]:
        return v
    docking[v] = find_parent(docking[v])
    return docking[v]


for i in range(P):
    datas.append(int(input()))


for data in datas:
    parent = find_parent(data)
    if parent == 0:
        break
    docking[parent] = docking[parent-1]
    res += 1

print(res)
