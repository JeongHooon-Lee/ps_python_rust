import sys

graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys. stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i,j))

def check_row(x,a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True
def check_col(x,a):
    for i in range(9):
        if a == graph[i][x]:
            return False
    return True

def check_box(x,y,a):
    nx = x//3*3
    ny = y//3*3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
    
    for i in range(1,10):
        x = blank[idx][0]
        y = blank[idx][1]

        if check_row(x,i) and check_col(y,i) and check_box(x,y,i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0 
dfs(0)