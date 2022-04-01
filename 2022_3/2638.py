import sys
from collections import deque
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
matrix : list = []
dy = [-1,0,1,0]
dx = [0,1,0,-1]
visited = [ [False]*M for _ in range(N) ]
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def dfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<M and (not visited[ny][nx]) and matrix[ny][nx] == 0:
            matrix[ny][nx] = 2
            visited[ny][nx] = True
            dfs(ny,nx)
            visited[ny][nx] = False

def bfs():
    queue = deque()
    for i in range(1,N-1):
        for j in range(1,M-1):
            if matrix[i][j] == 1:
                cnt = 0
                for k in range(4):
                    ny = i+dy[k]
                    nx = j+dx[k]
                    if matrix[ny][nx] == 2:
                        cnt+=1
                if cnt >= 2:
                    queue.append((i,j))
    while queue:
        y, x = queue.pop()
        dfs(y,x)
        matrix[y][x] = 2
def is_end():
    for i in range(1,N-1):
        for j in range(1,M-1):
            if matrix[i][j] == 1:
                return False
    return True

res = 0
while True:
    if is_end():
        print(res)
        break
    dfs(0,0)
    bfs()
    res +=1
    # print()
    # for i in matrix:
    #     print(*i)
