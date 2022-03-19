import sys
import heapq

INF = sys.maxsize
N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
v1, v2 = map(int, sys.stdin.readline().split())
def djkstra(start):
    dp = [INF]*(N+1)
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0,start))

    while heap:
        current_value, current_inx = heapq.heappop(heap)

        if current_value > dp[current_inx]:
            continue
            
        for next_value, next_inx in graph[current_inx]:
            new_value = next_value + current_value
            if new_value < dp[next_inx]:
                dp[next_inx] = new_value
                heapq.heappush(heap, (new_value, next_inx))
    return dp
from1 = djkstra(1)
fromv1 = djkstra(v1)
fromv2 = djkstra(v2)
temp = min(from1[v1]+fromv1[v2]+fromv2[N],from1[v2]+fromv2[v1]+fromv1[N])
print(temp if temp < INF else -1)