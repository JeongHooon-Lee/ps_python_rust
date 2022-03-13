import sys
import math 
INF = math.inf
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [ [None]*N for _ in range(N) ]
matrix = [ [INF]*N for _ in range(N) ]
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if matrix[a-1][b-1] > c:
        matrix[a-1][b-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if matrix[i][j] > matrix[i][k]+matrix[k][j]:
                matrix[i][j] = matrix[i][k]+matrix[k][j]
                graph[i][j] = k

for i in range(N):
    for j in range(N):
        print(0 if matrix[i][j] == INF else matrix[i][j], end=" ")
    print()

def func(start, end):
    if start == end:
        return []
    now = graph[start][end]
    if now is None:
        return [start+1, end+1]
    return func(start,now)[:-1] + func(now, end)

for i in range(N):
    for j in range(N):
        if matrix[i][j] == INF:
            print(0)
            continue
        else:
            res = func(i,j)
            print(len(res), *res)
