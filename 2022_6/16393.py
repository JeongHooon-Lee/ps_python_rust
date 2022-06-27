import sys

N = int(input())
edges: list = []
matrix: list = []
parents = {i: i for i in range(N)}
res: list = []

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N-1):
    for j in range(i+1, N):
        edges.append((matrix[i][j], i, j))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


edges.sort()
for value, depart, desti in edges:
    depart_parents = find_parents(depart)
    desti_parents = find_parents(desti)
    if depart_parents != desti_parents:
        parents[depart_parents] = parents[desti_parents] = min(
            depart_parents, desti_parents)
        res.append([depart+1, desti+1])

for i in res:
    print(*i)
