import sys
import heapq

N = int(input())
left_heap = []
right_heap = []
for i in range(N):
    X = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -X)
    elif len(left_heap) > len(right_heap):
        heapq.heappush(right_heap, X)
    
    if left_heap and right_heap and -left_heap[0] > right_heap[0]:
        max_temp = heapq.heappop(left_heap)
        min_temp = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -min_temp)
        heapq.heappush(right_heap, -max_temp) 
    
    print(-left_heap[0])