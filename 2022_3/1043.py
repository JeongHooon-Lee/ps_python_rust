import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
queue = deque()
queue += sys.stdin.readline().split()
visited = [False] * (M+1)
graph = [ [] for _ in range(N+1) ]
party_graph = [ [] for _ in range(M+1) ]

for i in range(1,M+1):
    temp = list(map(int, sys.stdin.readline().split()))
    party_graph[i]+=temp[1:]
    for j in temp[1:]:
        graph[j].append(i)

if queue[0] == "0":
    print(M)
    quit()
queue.popleft()

know : list = [0]*51
for i in queue:
    know[int(i)] =1

res = M
def func():
    global queue, res
    queue = list(map(int, queue))

    while queue:
        member = queue.pop()

        for party in graph[member]:
            for j in party_graph[party]:
                if not know[j]:
                    know[j] = 1
                    queue.append(j)
            if visited[party] == True:
                continue
            else:
                visited[party] = True
                res -= 1
func()          
print(res)
    