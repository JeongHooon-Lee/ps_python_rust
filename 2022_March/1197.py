import sys

V, E = map(int, sys.stdin.readline().split())
cycle_table = [i for i in range(V+1)]
edges : list = []


for i in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((A,B,C))
edges.sort(key = lambda x : x[2])

def func(vertex):
    if vertex != cycle_table[vertex]:
        cycle_table[vertex] = func(cycle_table[vertex])
    return cycle_table[vertex]

res = 0
for start, depart, value in edges:
    parents_of_start = func(start)
    parents_of_depart = func(depart)
    if parents_of_depart != parents_of_start:
        cycle_table[parents_of_depart] = cycle_table[parents_of_start] = min(parents_of_depart,parents_of_start)
        res += value
print(res)