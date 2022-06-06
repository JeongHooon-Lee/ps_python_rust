import heapq
import sys

N = int(input())
M = int(input())
edges: list = []
parents = {i: i for i in range(N+1)}
res = 0
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (c, a, b))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while edges:
    value, a, b = heapq.heappop(edges)
    parents_a = find_parents(a)
    parents_b = find_parents(b)
    if parents_a != parents_b:
        parents[parents_a] = parents[parents_b] = min(parents_b, parents_a)
        res += value

print(res)
