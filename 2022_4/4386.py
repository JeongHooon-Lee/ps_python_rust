from calendar import c
import sys
import math
N = int(sys.stdin.readline())
vertex : list = []
edges : list =[]
for i in range(N):
    vertex.append(list(map(float, sys.stdin.readline().split())))

def distance(first : int , second : int) -> float:
    return math.sqrt(((vertex[first][0]-vertex[second][0])**2)+
                     ((vertex[first][1]-vertex[second][1])**2))

for i in range(N):
    for j in range(i+1,N):
        edges.append([distance(i,j), i, j])

edges.sort()
cycle = [i for i in range(N)]

def find_parents(v):
    if v == cycle[v]:
        return v
    else:
        cycle[v] = find_parents(cycle[v])
        return cycle[v]

res = 0
for edge in edges:
    from_parent = find_parents(edge[1])
    to_parent = find_parents(edge[2])
    if from_parent != to_parent:
        next_parent = min(from_parent,to_parent)
        cycle[from_parent] = cycle[to_parent] = next_parent
        res += edge[0]

print(round(res,2))