import sys
R, C, T = map(int , sys.stdin.readline().split())
matrix : list = []
dy = [-1,0,1,0]
dx = [0,1,0,-1]
for i in range(R):
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] == -1:
        purifiler = i
    matrix.append(temp)
    
def merge(list1, list2):
    for i in range(R):
        for j in range(C):
            list1[i][j] += list2[i][j]
def purifiler_on():
    for i in range(purifiler-3,-1,-1):
        matrix[i+1][0] = matrix[i][0]
    for i in range(purifiler+2,R):
        matrix[i-1][0] = matrix[i][0]
    for i in range(1,C):
        matrix[0][i-1] = matrix[0][i]
        matrix[R-1][i-1] = matrix[R-1][i]
    for i in range(R-2,purifiler-1,-1):
        matrix[i+1][C-1] = matrix[i][C-1]
    for i in range(1, purifiler):
        matrix[i-1][C-1] = matrix[i][C-1]
    for i in range(C-2, 0, -1):
        matrix[purifiler][i+1] = matrix[purifiler][i]
        matrix[purifiler-1][i+1] = matrix[purifiler-1][i]
    matrix[purifiler-1][1] = 0
    matrix[purifiler][1] = 0
def sum_mise():
    sum = 0
    for i in range(R):
        for j in range(C):
            if matrix[i][j] != -1 and matrix[i][j] != 0:
                sum += matrix[i][j]
    return sum
for _ in range(T):
    temp = [ [0]*C for _ in range(R) ]
    for i in range(R):
        for j in range(C):
            if matrix[i][j] != -1 and matrix[i][j] != 0:
                value = matrix[i][j]//5
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0<=ny<R and 0<=nx<C and matrix[ny][nx] != -1:
                        temp[ny][nx] += value
                        matrix[i][j] -= value
    merge(matrix,temp)
    purifiler_on()
print(sum_mise())