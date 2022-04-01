import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

graph = [ [] for _ in range(N) ]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

mom = [None]*N
visited = [False]*N
def dfs(vertex):
    for i in graph[vertex]:
        if not visited[vertex]:
            visited[vertex] = True
            if not mom[i]:
                mom[i]=vertex+1
            dfs(i)
            visited[vertex] = False
dfs(0)
for i in mom[1:]:
    print(i)