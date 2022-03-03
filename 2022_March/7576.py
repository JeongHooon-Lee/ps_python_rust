import sys
from collections import deque
M, N = map(int, sys.stdin.readline().split())
matrix : list = []
dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs():
    queue = deque()
    temp_queue = deque()
    day = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                queue.append([i,j])
    
    while queue:
        temp = queue.popleft()
        for i in range(4):
            y = temp[0]+dy[i]
            x = temp[1]+dx[i]
            if 0 <= y < N and 0 <= x < M and matrix[y][x] == 0:
                temp_queue.append([y,x])
                matrix[y][x] = 1
        if not queue:
            day += 1
            for i in temp_queue:
                queue.append(i)
            temp_queue = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                print(-1)
                return
    print(day-1)

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

bfs()