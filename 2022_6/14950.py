import heapq
import sys

N, M, t = map(int, sys.stdin.readline().split())
edges: list = []
parents = {i: i for i in range(N+1)}
res = 0
temp = 0


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (C, A, B))

while edges:
    value, a, b = heapq.heappop(edges)
    parents_a = find_parents(a)
    parents_b = find_parents(b)
    if parents_a != parents_b:
        parents[parents_a] = parents[parents_b] = min(parents_b, parents_a)
        res += (value+temp)
        temp += t

print(res)
