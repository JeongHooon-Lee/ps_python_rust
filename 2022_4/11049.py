# pypy
import sys

N = int(input())
matrixs : list = []
for i in range(N):
    matrixs.append(list(map(int, sys.stdin.readline().split())))
dp = [[0]*N for _ in range(N)]

for i in range(1, N):
    for j in range(N-i):
        if i == 1:
            dp[j][j+i] = matrixs[j][0]*matrixs[j][1]*matrixs[j+1][1]
            continue
        
        dp[j][j+i] = 2**32
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], 
                           dp[j][k]+dp[k+1][j+i]+matrixs[j][0]*matrixs[k][1]*matrixs[j+i][1])

print(dp[0][N-1])

