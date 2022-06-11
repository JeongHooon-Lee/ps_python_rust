import heapq
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    h1, h2, k = map(int, sys.stdin.readline().split())
    graph[h1].append((k, h2))
    graph[h2].append((k, h1))

def dijkstra(v:int)->int:
    queue = []
    heapq.heappush(queue, (-sys.maxsize, v))
    visited[v] = sys.maxsize
    
    while queue:
        value, current = heapq.heappop(queue)
        value = -value
        if visited[current] > value:
            continue
        for next_value, next_current in graph[current]:
            min_value = min(value, next_value)
            if visited[next_current] < min_value:
                visited[next_current] = min_value
                heapq.heappush(queue, (-min_value, next_current))
dijkstra(S)
print(visited[E])
