import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
edges: list = []
parents = {i: i for i in range(N+1)}
res = 0
is_checked: dict = {}

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (c, a, b))

escape = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    heapq.heappush(edges, (escape[i], i+1, 0))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while edges:
    value, start, depart = heapq.heappop(edges)
    start_parents = find_parents(start)
    depart_parents = find_parents(depart)
    if start_parents != depart_parents:
        parents[start_parents] = parents[depart_parents] = min(
            start_parents, depart_parents)
        res += value

print(res)
