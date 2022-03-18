import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())

matrix : list = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

chicken : list = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            chicken.append((i,j))
            matrix[i][j] = 0
res = 1000000
for k in combinations(range(len(chicken)), M):
    temp_res2 = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                temp_res : int = 1000000
                for m in k:
                    temp_res = min(temp_res, abs(i-chicken[m][0])+abs(j-chicken[m][1]))
                temp_res2 += temp_res

    res = min(res, temp_res2)
print(res)