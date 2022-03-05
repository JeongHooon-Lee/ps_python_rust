import sys

N=int(input())
matrix =[ [0]*N for _ in range(N)]
visited = [False]*N
graph = [[] for _ in range(N)]

for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            graph[i].append(j)

def dfs(N): 
    for i in graph[N]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [False]*N