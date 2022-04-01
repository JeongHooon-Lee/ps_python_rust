import sys
N,M = map(int, sys.stdin.readline().split())
dp = [ [0]*101 for _ in range(101)]

dp[M][M] = 1

for i in range(M+1,N+1):
    dp[i][M] = (dp[i-1][M]*i)//(i-M)
print(dp[N][M])