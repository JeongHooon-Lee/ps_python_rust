import heapq
import sys


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while True:
    M, N = map(int, sys.stdin.readline().split())
    if M == 0 and N == 0:
        break
    edges: list = []
    res = 0
    for i in range(N):
        x, y, z = map(int, sys.stdin.readline().split())
        heapq.heappush(edges, ((z, x, y)))

    parents = {i: i for i in range(N)}
    while edges:
        value, start, end = heapq.heappop(edges)
        parents_start = find_parents(start)
        parents_end = find_parents(end)
        if parents_start != parents_end:
            parents[parents_start] = parents[parents_end] = min(
                parents_start, parents_end)
        else:
            res += value
    print(res)
