import sys
import math
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(input())
graph = [ [] for _ in range(V+1) ]
dp = [math.inf]*(V+1) 

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w,v))

def djkstra():
    heap = []
    heapq.heappush(heap, (0, K))
    dp[K] = 0
    
    while heap:
        current_value, current_inx = heapq.heappop(heap)

        if current_value > dp[current_inx]:
            continue

        for next_value, next_inx in graph[current_inx]:
            new_value = next_value + current_value

            if dp[next_inx] > new_value:
                dp[next_inx] = new_value
                heapq.heappush(heap, (new_value, next_inx))
djkstra()
for i in range(1,V+1):
    print("INF" if dp[i] == math.inf else dp[i])
