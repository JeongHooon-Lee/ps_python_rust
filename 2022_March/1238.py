import sys
import heapq
INF = 1000000

N,M,X = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
def djkstra(start):
    dp = [INF]*(N+1)
    dp[start] = 0
    heap = [] 
    heapq.heappush(heap, (dp[start], start))

    while heap:
        value, inx = heapq.heappop(heap)
        
        if value > dp[inx]:
            continue

        for next_value, next_inx in graph[inx]:
            new_value = next_value+value
            if dp[next_inx] > new_value:
                dp[next_inx] = new_value
                heapq.heappush(heap, (dp[next_inx], next_inx))
    return dp
from_X = djkstra(X)
res = 0
for i in range(1,N+1):
    if i==X:
        continue
    res = max(res, from_X[i] + djkstra(i)[X])
print(res)

###########################################################
# TLE
# import sys
# INF = 1000000
# N, M, X = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(N+1)]
# dp = [ [INF]*(N+1) for _ in range(N+1)]
# for i in range(M):
#     a, b, c = map(int, sys.stdin.readline().split())
#     dp[a][b]=c
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if i==j:
#             dp[i][j] = 0
# for k in range(1,N+1):
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
# res = 1
# for i in range(1,N+1):
#     res = max(dp[i][X]+dp[X][i],res)
# print(res)