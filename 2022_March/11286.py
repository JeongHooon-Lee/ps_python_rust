import sys
import heapq

N = int(input())
queue = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0: 
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])
    else:
        heapq.heappush(queue, (abs(x),x))
    