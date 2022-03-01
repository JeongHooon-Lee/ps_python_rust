import sys

N, K = map(int, sys.stdin.readline().split())
dp = [0]*(N+1)
dp[0] = dp[1] = 1
for i in range(2,N+1):
    dp[i] = dp[i-1]*i
print(int(dp[N]//(dp[N-K]*dp[K]))%10007)