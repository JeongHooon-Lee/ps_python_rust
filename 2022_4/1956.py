# pypy
import sys

V, E = map(int, sys.stdin.readline().split())
edges = [[sys.maxsize]*(V+1) for _ in range(V+1)]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            edges[i][j] = min(edges[i][k] + edges[k][j], edges[i][j])

res = sys.maxsize
for i in range(1, V+1):
    for j in range(1, V+1):
        res = min(edges[i][j] + edges[j][i], res)
if res == sys.maxsize:
    print(-1)
else:
    print(res)
