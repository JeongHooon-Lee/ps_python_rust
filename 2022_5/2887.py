import sys

N = int(sys.stdin.readline())
data: list = []
edges: list = []
union = [i for i in range(N)]

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    data.append(temp+[i])

for i in range(3):
    data.sort(key=lambda x: x[i])
    for j in range(1, N):
        edges.append(
            (abs(data[j-1][i] - data[j][i]), data[j-1][3], data[j][3]))

edges.sort()


def func(vertex):
    if vertex != union[vertex]:
        union[vertex] = func(union[vertex])
    return union[vertex]


res = 0

for value, start, depart in edges:
    parents_of_start = func(start)
    parents_of_depart = func(depart)
    if parents_of_depart != parents_of_start:
        union[parents_of_depart] = union[parents_of_start] = min(
            parents_of_depart, parents_of_start)
        res += value
print(edges)
print(res)
