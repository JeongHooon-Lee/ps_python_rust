import heapq
import sys

T = int(input())


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for i in range(T):
    N, M, p, q = map(int, sys.stdin.readline().split())
    edges: list = []
    res = 0
    parents = {k: k for k in range(N+1)}
    for j in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        heapq.heappush(edges, (w, u, v))

    while edges:
        value, start, depart = heapq.heappop(edges)
        start_parents = find_parents(start)
        depart_parents = find_parents(depart)
        if start_parents != depart_parents:
            parents[start_parents] = parents[depart_parents] = min(
                start_parents, depart_parents)
            if start == p and depart == q:
                res = 1
    print("YES" if res == 1 else "NO")
