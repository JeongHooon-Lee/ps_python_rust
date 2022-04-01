import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1) 

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
    print(start, end= " ")

for i in range(1,N+1):
    if not visited[i]:
        visited[i] = True
        dfs(i)