import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
graph = [ [] for _ in range(N) ] 
visited = [False]*N

def dfs(inx):
    if visited[inx]:
        return 0
    visited[inx] = True
    for i in graph[inx]:
        if not visited[i]:
            dfs(i)
    return 1

for i in range(M):
    a = list(map(int,sys.stdin.readline().split()))
    graph[a[0]-1].append(a[1]-1)
    graph[a[1]-1].append(a[0]-1)

res = 0
for i in range(N):
    res+=dfs(i)
print(res)