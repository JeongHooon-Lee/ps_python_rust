import sys
sys.setrecursionlimit(10**6)

N = int(input().strip())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[N])
