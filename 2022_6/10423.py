import heapq
import sys

N, M, K = map(int, sys.stdin.readline().split())
edges: list = []
power = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (w, u, v))

parents = {i: i for i in range(N+1)}
res = 0


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while edges:
    value, start, end = heapq.heappop(edges)
    start_parents = find_parents(start)
    end_parents = find_parents(end)
    if start_parents != end_parents:
        if start_parents not in power and end_parents not in power:
            parents[start_parents] = parents[end_parents] = min(
                start_parents, end_parents)
        elif start_parents in power and end_parents in power:
            continue
        elif start_parents in power and end_parents not in power:
            parents[start_parents] = parents[end_parents] = start_parents
        elif start_parents not in power and end_parents in power:
            parents[start_parents] = parents[end_parents] = end_parents
        res += value

print(res)
