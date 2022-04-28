import enum
import sys

N, M = map(int, sys.stdin.readline().split())
union = [i for i in range(N)]
edges: list = []


def find_parents(vertex):
    if vertex == union[vertex]:
        return vertex
    else:
        y = find_parents(union[vertex])
        union[vertex] = y
        return y


for i in range(M):
    edges.append(list(map(int, sys.stdin.readline().split())))

res = 0
for i, info in enumerate(edges):
    parent_of_start = find_parents(info[0])
    parent_of_depart = find_parents(info[1])
    if parent_of_depart != parent_of_start:
        union[max(parent_of_depart, parent_of_start)] = min(
            parent_of_start, parent_of_depart)
    elif res == 0:
        res = i+1

print(res)
