import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
visited = [-1] * 101
graph = [ i for i in range(101) ]

for i in range(N+M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u] = v

queue = deque()
queue.append(1)
visited[1] = 0

while queue:
    x = queue.popleft()

    for i in range(1,7):
        y = x+i
        if y>100:
            continue
        y = graph[y]

        if visited[y] == -1 or visited[y]>visited[x]+1:
            visited[y] = visited[x]+1
            queue.append(y)

print(visited[-1])