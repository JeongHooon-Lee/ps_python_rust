import sys
from collections import deque

dy = [-1,0,1,0]
dx = [0,-1,0,1]
level = 2
exp = 0
N = int(input())
matrix : list = []
inx_sang : list = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    if 9 in temp:
        inx_sang.append(i)
        inx_sang.append(temp.index(9))
    matrix.append(temp)

def bfs(i,j):
    queue = deque()
    queue.append((i, j, 0))
    visited = [ [False]*N for _ in range(N) ]
    eat = []
    while queue:
        y, x, c = queue.popleft()

        for i in range(4):
            temp_y = y+dy[i]
            temp_x = x+dx[i]
            if 0<=temp_y<N and 0<=temp_x<N and visited[temp_y][temp_x] == False:
                if matrix[temp_y][temp_x]<=level or matrix[temp_y][temp_x] == 0:
                    queue.append((temp_y,temp_x,c+1))
                    visited[temp_y][temp_x] = True
                if matrix[temp_y][temp_x] < level and matrix[temp_y][temp_x] != 0:
                    eat.append([temp_y,temp_x,c+1])
    if not eat:
        return -1
    eat.sort(key = lambda x: (x[2], x[0], x[1]))
    return eat[0]
res = 0

while True:
    temp = bfs(inx_sang[0],inx_sang[1])
    if type(temp) == int:
        print(res)
        break
    else:
        res += temp[2]
        matrix[inx_sang[0]][inx_sang[1]] = 0
        inx_sang[0], inx_sang[1] = temp[0], temp[1]
        matrix[temp[0]][temp[1]] = 0
        exp+=1
        if exp == level:
            level+=1
            exp = 0

