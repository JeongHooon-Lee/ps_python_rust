import sys

N, M = map(int, sys.stdin.readline().split())
start = min(N, M)
matrix: list = []
for i in range(N):
    matrix.append(list(map(int, list("".join(sys.stdin.readline().strip())))))

for k in range(start, 0, -1):
    start = k
    for i in range(N-start+1):
        for j in range(M-start+1):
            if matrix[i][j] == matrix[i+start-1][j] == matrix[i][j+start-1] == matrix[i+start-1][j+start-1]:
                print(start**2)
                exit()
