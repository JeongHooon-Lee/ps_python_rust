import heapq
import sys

N = int(input())


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for _ in range(N):
    N, M = map(int, sys.stdin.readline().split())
    parents = {i: i for i in range(N)}
    edges: list = []
    xor_res = 0
    for i in range(1, N):
        u, c = map(int, sys.stdin.readline().split())
        heapq.heappush(edges, (c, i, u))

    for i in range(M):
        res = 0
        u, v, c = map(int, sys.stdin.readline().split())
        heapq.heappush(edges, (c, u, v))
        temp_edges = edges.copy()

        while temp_edges:
            value, start, depart = heapq.heappop(temp_edges)
            start_parents = find_parents(start)
            depart_parents = find_parents(depart)
            if start_parents != depart_parents:
                parents[start_parents] = parents[depart_parents] = min(
                    start_parents, depart_parents)
                res += value
        xor_res ^= res
    print(xor_res)
