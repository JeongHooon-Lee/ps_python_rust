import sys

N, M = map(int, sys.stdin.readline().split())
matrix: list = []
for i in range(N):
    matrix.append(list("".join(sys.stdin.readline().strip())))

left = right = 0
for i in range(N):
    temp = 1
    for j in range(M):
        if matrix[i][j] == "X":
            temp = 0
            break
    if temp:
        left += 1

for j in range(M):
    temp = 1
    for i in range(N):
        if matrix[i][j] == "X":
            temp = 0
            break
    if temp:
        right += 1

print(max(left, right))
