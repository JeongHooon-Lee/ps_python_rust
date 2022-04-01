import sys
from collections import deque
A, B = map(int, sys.stdin.readline().split())

def bfs():
    queue = deque()
    queue.append((A,0))

    res = 10000000
    while queue:
        num, cnt = queue.popleft()
        if num == B:
            res = min(res, cnt)
            continue
        if num*2 <= B:
            queue.append((num*2,cnt+1))
        if num*10+1 <= B:
            queue.append((num*10+1,cnt+1))
    print(-1 if res == 10000000 else res+1)

bfs()