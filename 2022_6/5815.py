import sys

N = int(input())
matrix: list = []
edges: list = []
parents = {i: i for i in range(N)}
res = 0
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
costs = list(map(int, sys.stdin.readline().split()))

for i in range(N-1):
    for j in range(i+1, N):
        edges.append((matrix[i][j], i, j))

edges.sort()


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for value, depart, desti in edges:
    depart_parents = find_parents(depart)
    desti_parents = find_parents(desti)
    if depart_parents != desti_parents:
        if costs[depart_parents] < costs[desti_parents]:
            min_value = depart_parents
        else:
            min_value = desti_parents
        max_value = depart_parents if min_value == desti_parents else desti_parents

        if value < costs[min_value] or costs[max_value] > value:
            parents[depart_parents] = parents[desti_parents] = min_value
            costs[depart_parents] = costs[desti_parents] = costs[min_value]
            res += value
# res_list = {i: [] for i in range(N)}
res_list = set([find_parents(i) for i in range(N)])
for i in res_list:
    res += costs[i]
print(res)
