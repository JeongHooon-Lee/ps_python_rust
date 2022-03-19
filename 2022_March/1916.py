import sys
import heapq
sys.setrecursionlimit(10**6)
N = int(input())
M = int(input())
INF = pow(N,100000)+1
graph =[ [] for _ in range(N+1) ]
dp = [INF]*(N+1)
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
A,B = map(int, sys.stdin.readline().split())
dp[A] = 0

def djkstra():
    global res
    heap = []
    heapq.heappush(heap, (0,A))

    while heap:
        cost, inx = heapq.heappop(heap)

        if dp[inx] < cost:
            continue

        for next_cost, next_inx in graph[inx]:
            new_cost = cost+next_cost
            if new_cost < dp[next_inx]:
                dp[next_inx] = new_cost
                heapq.heappush(heap, (new_cost,next_inx))
    return(dp)
print(djkstra()[B])