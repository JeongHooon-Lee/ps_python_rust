import sys

sys.setrecursionlimit(10**6)
N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort(reverse=True)

res = [0] * (N+1)
temp = 1


def dfs(V):
    global temp
    res[V] = temp
    temp += 1
    visited[V] = True

    for target in graph[V]:
        if not visited[target]:
            dfs(target)


dfs(R)

for i in range(1, N+1):
    print(res[i])
