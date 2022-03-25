import sys
sys.setrecursionlimit(10**6)

def dfs(start):
    max_of_graph = 0
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            max_of_graph = max(max_of_graph, dfs(i))
        else:
            max_of_graph = max(max_of_graph, dp[i])
    
    dp[start] = max_of_graph + dp[start]
    return dp[start]


for i in range(int(sys.stdin.readline())):
    N, K = map(int, sys.stdin.readline().split())
    dp = [-1] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (N+1)
    graph = [ [] for _ in range(N+1) ]
    for i in range(K):
        pre_vertex, post_vertex = map(int, sys.stdin.readline().split())
        graph[post_vertex].append(pre_vertex)
    W = int(input())

    print(dfs(W))
