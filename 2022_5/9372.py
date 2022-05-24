import sys


def dfs(v, cnt):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            cnt = dfs(i, cnt+1)

    return cnt


for i in range(int(input())):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(dfs(1, 0))
