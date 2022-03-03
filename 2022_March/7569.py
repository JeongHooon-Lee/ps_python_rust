import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())

matrix : list = [[[0]*M for _ in range(N)]for _ in range(H)]
dx = [0,1,0,-1,0,0]
dy = [-1,0,1,0,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    queue = deque()
    temp_queue = deque()
    day = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if matrix[i][j][k] == 1:
                    queue.append([i,j,k])
    
    while queue:
        temp = queue.popleft()
        for i in range(6):
            z = temp[0]+dy[i]
            y = temp[1]+dx[i]
            x = temp[2]+dz[i]
            if 0 <= y < N and 0 <= x < M and 0<= z < H and matrix[z][y][x] == 0:
                temp_queue.append([z,y,x])
                matrix[z][y][x] = 1
        if not queue:
            day += 1
            for i in temp_queue:
                queue.append(i)
            temp_queue = deque()

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if matrix[i][j][k] == 0:
                    print(-1)
                    return
    print(day-1)

for i in range(H):
    for j in range(N):
        matrix[i][j] = list(map(int, sys.stdin.readline().split()))
bfs()