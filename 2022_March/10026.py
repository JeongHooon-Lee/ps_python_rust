import sys
sys.setrecursionlimit(10**6)
matrix : list = []
dx = [0,1,0,-1]
dy = [-1,0,1,0]


N = int(input())
visited = [ [False]*N for _ in range(N) ]

for i in range(N):
    matrix.append(" ".join(sys.stdin.readline()).split())

def dfs(a,b,version):
    if visited[a][b] == True:
        return 0
    visited[a][b] = True
    for i in range(4):
        temp_y = a+dy[i]
        temp_x = b+dx[i]
        if version == 0:
            if 0<=temp_y<N and 0<= temp_x < N and not visited[temp_y][temp_x] and matrix[a][b] == matrix[temp_y][temp_x]:
                    dfs(temp_y,temp_x,0)
        else:
            if 0<=temp_y<N and 0<= temp_x < N and not visited[temp_y][temp_x]:
                if (matrix[a][b] == 'R' or matrix[a][b] == 'G') and (matrix[temp_y][temp_x] == 'R' or matrix[temp_y][temp_x] == 'G'):
                    dfs(temp_y,temp_x,1)
                elif matrix[a][b] == "B" and matrix[temp_y][temp_x] == "B":
                    dfs(temp_y,temp_x,1)
    return 1


res = [0,0]
for i in range(N):
    for j in range(N):
        res[0] += dfs(i,j,0)
visited = [ [False]*N for _ in range(N) ]

for i in range(N):
    for j in range(N):
        res[1] += dfs(i,j,1)

print(*res)