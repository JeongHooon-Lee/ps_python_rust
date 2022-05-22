import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

res = [0] * (N+1)


def bfs(R):
    queue = deque()
    queue.append(R)
    visited = [False] * (N+1)
    visited[R] = True
    temp = 1
    res[R] = temp

    while queue:
        v = queue.popleft()
        for vertex in graph[v]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
                temp += 1
                res[vertex] = temp

    for i in range(1, N+1):
        print(res[i])


bfs(R)
