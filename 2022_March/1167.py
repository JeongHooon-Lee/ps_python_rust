import sys
sys.setrecur
V = int(input())
graph = [ [] for _ in range(V+1) ] 
for i in range(V):
    temp = list(map(int, sys.stdin.readline().split()))[:-1]
    vert = temp[0]
    temp = temp[1:]
    for j in range(0,len(temp),2):
        graph[vert].append((temp[j],temp[j+1]))

def dfs(dot, value):
    for a,b in graph[dot]:
        if distance[a] == -1:
            distance[a] = value+b
            dfs(a,value+b)

distance = [-1]*(V+1)
dfs(1,0)
temp = distance.index(max(distance))
distance = [-1]*(V+1)
distance[temp] = 0
dfs(temp,0)
print(max(distance))