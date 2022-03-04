import sys

N, M = map(int, sys.stdin.readline().split())

dp = list(map(int, sys.stdin.readline().split()))
for i in range(1,N):
    dp[i] = dp[i-1]+dp[i]
dp = [0] + dp
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[b]-dp[a-1])