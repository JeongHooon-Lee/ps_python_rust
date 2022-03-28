import sys

N = int(sys.stdin.readline())
numbers = [-1] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
matrix = [ [0]*(N+1) for _ in range(N+1) ]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i==j:
            matrix[i][j] = 1
for i in range(N-1, 0, -1):
    for j in range(i+1, N+1):
        if j == i+1 and numbers[j] == numbers[i]:
            matrix[i][j] = 1
            continue
        elif numbers[i] == numbers [j] and matrix[i+1][i+1] and matrix[i+1][j-1]:
            matrix[i][j] = 1
for i in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(matrix[S][E])
'''
1 2 1 3 1 2 1


1 0 1 0 0 0 1
0 1 0 0 0 1 0
0 0 1 0 1 0 0
0 0 0 1 0 0 0
0 0 0 0 1 0 1
0 0 0 0 0 1 0
0 0 0 0 0 0 1
'''