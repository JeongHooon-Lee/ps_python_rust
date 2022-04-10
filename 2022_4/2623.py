import sys
import heapq
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
degree = [0]*(N+1)
queue = []
res = []
for i in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    length = data[0]
    for i in range(1,length):
        graph[data[i]].append(data[i+1])
        degree[data[i+1]] += 1

for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(queue, i)
        
while queue:
    temp = heapq.heappop(queue)
    res.append(temp)
    for i in graph[temp]:
        degree[i] -=1
        if degree[i] == 0:
            heapq.heappush(queue, i)

if not queue and degree.count(0) != N+1:
    print(0)
else:
    for i in res:
        print(i)