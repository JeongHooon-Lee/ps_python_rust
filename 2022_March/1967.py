import sys
sys.setrecursionlimit(10**6)
N = int(input())
graph = [ [] for _ in range(N) ]

for i in range(N-1):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

def dfs(vertex,value):
    for a,b in graph[vertex]:
        if distance[a] == -1:
            distance[a] = value +b
            dfs(a,value+b)

distance = [-1] * N
dfs(0,0)
temp = distance.index(max(distance))
distance = [-1] * N
distance[temp] = 0
dfs(temp,0)
print(max(distance))