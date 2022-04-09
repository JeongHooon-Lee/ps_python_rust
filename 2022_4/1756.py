import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
Degree = [ 0 for _ in range(N+1) ]
graph = [[] for _ in range(N+1)]
queue = []
res = []

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    Degree[B] +=1
    
for i in range(1, N+1):
    if Degree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    res.append(tmp)
    for i in graph[tmp]:
        Degree[i] -= 1
        if Degree[i] == 0:
            heapq.heappush(queue, i)
            
print(" ".join(map(str, res)))

# 못품
# 출처: https://hongcoding.tistory.com/94