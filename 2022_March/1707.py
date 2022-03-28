import sys
from collections import deque

def bfs(V):
    queue = deque()
    queue.append((V, 1))
    visited[V] = 1

    while queue:
        vertex, status = queue.popleft()
        
        new_status = -status
        for i in graph[vertex]:
            if not visited[i]:
                visited[i] = new_status
                queue.append((i, new_status))
            elif visited[i]:
                if status == visited[i]:
                    return -1
    return 1
    
K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    visited = [0] * (V+1)
    graph = [ [] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    res = 1
    for i in range(1,V+1):
        if not visited[i]:
            if bfs(i) == -1:
                res = -1
                break
    if res == -1:
        print("NO")
    else:
        print("YES")
        

