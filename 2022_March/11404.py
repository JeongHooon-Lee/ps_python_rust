import sys

N = int(input())
M = int(input())
dp = [ [10000000]*N for _ in range(N)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if dp[a-1][b-1] > c:
        dp[a-1][b-1] = c
for i in range(N):
    for j in range(N):
        if i== j:
            dp[i][j] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for i in range(N):
    for j in range(N):
        if dp[i][j] == 10000000:
            dp[i][j] = 0
for i in dp:
    print(*i)


