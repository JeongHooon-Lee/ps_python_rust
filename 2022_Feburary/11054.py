from re import L
import sys

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
dp = [ [0] * N for _ in range(2) ]

for i in range(N):
    for j in range(i):
        if data[i] > data[j] and dp[0][i] < dp[0][j]:
            dp[0][i] = dp[0][j]
    dp[0][i]+=1
data.reverse()
for i in range(N):
    for j in range(i):
        if data[i] > data[j] and dp[1][i] < dp[1][j]:
            dp[1][i] = dp[1][j]
    dp[1][i]+=1

answer = 0
for i in range(N):
    if answer < dp[0][i] + dp[1][N-i-1]:
        answer = dp[0][i] + dp[1][N-i-1]
print(answer -1)
