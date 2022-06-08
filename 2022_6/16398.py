import heapq
import sys

N = int(input())
edges: list = []
res = 0
parents = {i: i for i in range(N)}

for i in range(N):
    input_data = list(map(int, sys.stdin.readline().split()))
    for j in range(i+1, N):
        heapq.heappush(edges, (input_data[j], i, j))


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
