import sys

N, M = map(int, sys.stdin.readline().split())
matrix : list= []
dy = [-1,0,1,0]
dx = [0,1,0,-1]
visited = [ [False]*M for _ in range(N) ]

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
res = 0 

def dfs(y,x,value,cnt):
    global res
    if cnt == 4:
        res = max(res, value)
        return 
    
    for i in range(4):
        temp_y = y+dy[i]
        temp_x = x+dx[i]
        if 0<=temp_y<N and 0<=temp_x<M and visited[temp_y][temp_x] == False:
            if cnt ==2:
                visited[temp_y][temp_x] = True
                dfs(y,x,value+matrix[temp_y][temp_x],cnt+1)
                visited[temp_y][temp_x] = False
            visited[temp_y][temp_x] = True
            dfs(temp_y,temp_x,value+matrix[temp_y][temp_x],cnt+1)
            visited[temp_y][temp_x] = False


for i in range(N):
    for j in range(M):
        if i == 2 and j == 8:
            visited[i][j] = True
            dfs(i,j,matrix[i][j],1)
            visited[i][j] = False
        else:
            visited[i][j] = True
            dfs(i,j,matrix[i][j],1)
            visited[i][j] = False

print(res)