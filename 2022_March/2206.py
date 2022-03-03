import sys
from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]
N, M = map(int, sys.stdin.readline().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, " ".join(sys.stdin.readline().strip()).split())))

def bfs():
    queue = deque()
    queue.append([0,0,1])
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1

    while queue:
        a, b, c = queue.popleft()
        if [N-1, M-1] == [a, b]:
            return visited[a][b][c]
        
        for i in range(4):
            y = a+dy[i]
            x = b+dx[i]
            if 0<=y<N and 0<=x<M:
                if matrix[y][x] == 1 and c == 1:
                    visited[y][x][0] = visited[a][b][c]+1
                    queue.append([y,x,0])
                elif matrix[y][x] == 0 and visited[y][x][c] == 0:
                    visited[y][x][c] = visited[a][b][c]+1
                    queue.append([y,x,c])
    return -1       

print(bfs())