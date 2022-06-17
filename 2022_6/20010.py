import heapq
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
edges: list = []
parents = {i: i for i in range(N)}
graph = [[] for _ in range(N)]
res = 0
res2 = 0

for i in range(K):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (c, a, b))


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
        graph[depart].append((start, value))
        graph[start].append((depart, value))


def bfs(v: int) -> int:
    global res2
    queue = deque()
    queue.append((v, 0))
    visited = [0]*N
    visited[v] = True

    while queue:
        now, cost = queue.popleft()
        for next_now, next_cost in graph[now]:
            new_cost = cost + next_cost
            if not visited[next_now]:
                res2 = max(res2, new_cost)
                queue.append((next_now, new_cost))
                visited[next_now] = True


for i in range(N):
    bfs(i)

print(res)
print(res2)
