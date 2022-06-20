import heapq
import sys

N = int(input())
matrix: list = []
parents = {i: i for i in range(N)}
edges: list = []
res = 0
res_list: list = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for i in range(N-1):
    for j in range(i+1, N):
        if matrix[i][j] < 0:
            parents_i = find_parents(i)
            parents_j = find_parents(j)
            parents[parents_i] = parents[parents_j] = min(parents_i, parents_j)
            res -= matrix[i][j]
        else:
            heapq.heappush(edges, (matrix[i][j], i, j))

while edges:
    value, start, depart = heapq.heappop(edges)
    parents_start = find_parents(start)
    parents_depart = find_parents(depart)
    if parents_start != parents_depart:
        parents[parents_start] = parents[parents_depart] = min(
            parents_start, parents_depart)
        res += value
        res_list.append((start+1, depart+1))

print(res, len(res_list))
for i in res_list:
    print(*i)
