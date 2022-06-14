import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
parents = {i: i for i in range(N+1)}
edges: list = []
total = 0
res = 0


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for i in range(M):
    start, depart, value = map(int, sys.stdin.readline().split())
    total += value
    heapq.heappush(edges, (value, start, depart))


while edges:
    value, start, depart = heapq.heappop(edges)
    parents_start = find_parents(start)
    parents_depart = find_parents(depart)
    if parents_start != parents_depart:
        parents[parents_start] = parents[parents_depart] = min(
            parents_start, parents_depart)
        res += value

res_list = set([find_parents(i) for i in range(1, N+1)])
if len(res_list) != 1:
    print(-1)
else:
    print(total-res)
