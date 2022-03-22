import sys
from collections import deque
N = int(input())

def bfs():
    queue = deque()
    queue.append(([N],0))
    res_history : list = []
    res_count = sys.maxsize
    while queue:
        history, cnt = queue.popleft()
        if history[-1] == 1 and cnt < res_count:
            res_history = history.copy()
            res_count = cnt
            continue
        if cnt >= res_count:
            continue
        last_data = history[-1]
        if last_data%3 == 0:
            queue.append((history+[last_data//3],cnt  + 1))
        if last_data%2 == 0:
            queue.append((history+[last_data//2],cnt + 1))
        queue.append((history+[last_data-1],cnt + 1))
        
    print(res_count)
    print(*res_history)
bfs()
# pypy