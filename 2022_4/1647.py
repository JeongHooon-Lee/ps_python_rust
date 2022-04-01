import sys

N, M = map(int, sys.stdin.readline().split())
edges : list = []
for i in range(M):
    edges.append(list(map(int, sys.stdin.readline().split())))
edges.sort(key = lambda x : x[2])

cycle_list = [i for i in range(N+1)]

def find_parents(vertex):
    if vertex != cycle_list[vertex]:
        cycle_list[vertex] = find_parents(cycle_list[vertex])    
    return cycle_list[vertex]

res = []
for start, depart, value in edges:
    parent_of_start = find_parents(start)
    parent_of_depart = find_parents(depart)
    if parent_of_depart != parent_of_start:
        cycle_list[parent_of_start] = cycle_list[parent_of_depart] = min(parent_of_depart, parent_of_start)
        res.append(value)
print(sum(res[:-1]))
