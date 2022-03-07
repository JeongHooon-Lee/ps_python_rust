import sys

N, M = map(int, sys.stdin.readline().split())
matrix : list= []
dx = [[1,2,3],[0,0,0],[1,1,0],[0,0,1],[1,2,0],[1,1,1],[0,-1,-2],[1,2,2],[1,0,0],[0,1,2],[0,0,-1],[0,1,1],[1,1,2],[0,-1,-1],[1,1,2],[1,2,1],[0,0,1],[0,0,-1],[-1,0,1]]
dy = [[0,0,0],[1,2,3],[0,1,1],[1,2,2],[0,0,1],[0,1,2],[-1,-1,-1],[0,0,-1],[0,1,2],[1,1,1],[1,2,2,],[1,1,2],[0,-1,-1],[1,1,2],[0,1,1],[0,0,1],[1,2,1],[1,2,1],[1,1,1]]
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

maxnum = 0
def func(a,b):
    global maxnum
    for i in range(19):
        res = matrix[a][b]
        for j in range(3):
            temp_a = a+dy[i][j]
            temp_b = b+dx[i][j]
            if not (0<=temp_a<N and 0<=temp_b<M):
                res = matrix[a][b]
                break
            res += matrix[temp_a][temp_b]
        maxnum = max(res, maxnum)

for i in range(N):
    for j in range(M):
        func(i,j)
print(maxnum)