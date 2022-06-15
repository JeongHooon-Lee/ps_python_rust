import heapq
import sys

N, M, K = map(int, sys.stdin.readline().split())
edges: list = []
res: list = [-1]

for i in range(1, M+1):
    x, y = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (i, x, y))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for i in range(K):
    if res[-1] == 0:
        res.append(0)
        continue
    temp_edges = edges.copy()
    parents = {i: i for i in range(N+1)}
    mst = 0
    while temp_edges:
        value, start, depart = heapq.heappop(temp_edges)
        start_parents = find_parents(start)
        depart_parents = find_parents(depart)
        if start_parents != depart_parents:
            parents[start_parents] = parents[depart_parents] = min(
                start_parents, depart_parents)
            mst += value
    temp = set([find_parents(i) for i in range(1, N+1)])
    if len(temp) != 1:
        res.append(0)
    else:
        res.append(mst)
    heapq.heappop(edges)

print(*res[1:])
