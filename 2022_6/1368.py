import heapq
import sys

N = int(input())
edges: list = []
parents = {i: i for i in range(N+1)}
res = 0
for i in range(1, N+1):
    data = int(sys.stdin.readline().strip())
    heapq.heappush(edges, (data, 0, i))

for i in range(1, N+1):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(i, N):
        heapq.heappush(edges, (data[j], i, j+1))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while edges:
    value, start, end = heapq.heappop(edges)
    parents_start = find_parents(start)
    parents_end = find_parents(end)
    if parents_start != parents_end:
        parents[parents_start] = parents[parents_end] = min(
            parents_start, parents_end)
        res += value
print(res)
