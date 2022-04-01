import sys
import copy
from collections import deque
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
dy = [-1,0,1,0]
dx = [0,1,0,-1]
matrix : list =[]
virused : list = []
cleaned : list = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        if temp[j] == 0:
            cleaned.append((i,j))
        elif temp[j]==2 :
            virused.append((i,j))
    matrix.append(temp)

def count_zero(a):
    res = 0
    for i in range(N):
        res += a[i].count(0)
    return res

def bfs(a,b,c):
    global res
    queue =deque()
    queue += virused
    square = copy.deepcopy(matrix)
    square[cleaned[a][0]][cleaned[a][1]] = 1
    square[cleaned[b][0]][cleaned[b][1]] = 1
    square[cleaned[c][0]][cleaned[c][1]] = 1
    visited =  [[False]*M for _ in range(N) ]
    while queue:
        y, x= queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                if square[ny][nx] != 1:
                    queue.append((ny,nx))
                    square[ny][nx] = 2
                    visited[ny][nx] = True
    res = max(count_zero(square), res)
res = -1
items = list(combinations([i for i in range(len(cleaned))], 3))
for i in items:
    bfs(i[0],i[1],i[2])
print(res)

#pypy