import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
collages = [0]+list(sys.stdin.readline().strip().split())
edges: list = []
parents = {i: i for i in range(N+1)}
res = 0

for i in range(M):
    u, v, d = map(int, sys.stdin.readline().split())
    if collages[u] != collages[v]:
        heapq.heappush(edges, (d, u, v))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while edges:
    value, start, end = heapq.heappop(edges)
    parents_start = find_parents(start)
    paretns_end = find_parents(end)
    if parents_start != paretns_end:
        parents[parents_start] = parents[paretns_end] = min(
            parents_start, paretns_end)
        res += value

res_list = set([find_parents(i) for i in range(1, N+1)])

if len(res_list) == 1:
    print(res)
else:
    print(-1)
