import sys
import heapq

N=int(input())
heap = []

for i in range(N):
    A = int(sys.stdin.readline())
    if A == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-A, A))