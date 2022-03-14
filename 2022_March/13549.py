import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
visited = [-1]*100001
def bfs():
    queue = deque()
    queue.append((N, 0))

    while queue:
        a, b= queue.popleft()
        if visited[a] != -1 and visited[a] < b:
            continue
        elif visited[a] == -1:
            visited[a] = b
        if a == K:
            return b
            
        if a*2 <= 100000:
            queue.append((a*2,b))
        if a-1 >= 0:
            queue.append((a-1,b+1))
        if a+1 <= 100000:
            queue.append((a+1,b+1))

if N > K:
    print(N-K)
else:
    print(bfs())