import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
A, B, C = map(int, sys.stdin.readline().split())
parents = {i: i for i in range(N+1)}
edges: list = []
edges2: list = []
res = 1 if C == 0 else 0
res2 = res
parents[1] = 0


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (-C, A, B))
    heapq.heappush(edges2, (C, A, B))

while edges:
    value, start, end = heapq.heappop(edges)
    start_parents = find_parents(start)
    end_parents = find_parents(end)
    if start_parents != end_parents:
        parents[start_parents] = parents[end_parents] = min(
            start_parents, end_parents)
        if value == 0:
            res += 1

parents = {i: i for i in range(N+1)}
parents[1] = 0

while edges2:
    value, start, end = heapq.heappop(edges2)
    start_parents = find_parents(start)
    end_parents = find_parents(end)
    if start_parents != end_parents:
        parents[start_parents] = parents[end_parents] = min(
            start_parents, end_parents)
        if value == 0:
            res2 += 1
print(res2**2-res**2)
