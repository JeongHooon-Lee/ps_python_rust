import sys
for i in range(int(input())):
    N = int(sys.stdin.readline())
    matrix : list = []
    for j in range(2):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    for j in range(1,N):
        if j == 1:
            matrix[0][j] += matrix[1][j-1]
            matrix[1][j] += matrix[0][j-1]
        else:
            matrix[0][j] += max(matrix[1][j-1],matrix[1][j-2])
            matrix[1][j] += max(matrix[0][j-1],matrix[0][j-2])
    print(max(matrix[0][N-1],matrix[1][N-1]))