import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
queue= deque([ i for i in range(1,N+1) ])
cnt = 0


for i in arr:
    temp = queue.index(i)
    if temp >= len(queue)-temp:
        cnt +=(len(queue)-temp)
        for i in range(len(queue)-temp):
            queue.appendleft(queue.pop())
        queue.popleft()
    elif temp < len(queue)-temp:
        cnt += temp
        for i in range(temp):
            queue.append(queue.popleft())
        queue.popleft()
print(cnt)

# 1 2 3 4 5 6 7 8 9 10
# 2 3 4 5 6 7 8 9 10 1*
# 3 4 5 6 7 8 9 10 1
# 9 10 1 3 4 5 6 7 8 ***
# 10 1 3 4 5 6 7 8
# ****