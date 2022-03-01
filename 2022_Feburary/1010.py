import sys

t = int(input())
dp = [0]*30
dp[0] = dp[1] = 1
for i in range(t):
    N, M = map(int, sys.stdin.readline().split())
    if not dp[max(N,M)]:
        for i in range(max(2,M+1)):
            if not dp[i]:
                dp[i] = dp[i-1]*i
    
    print(dp[M]//(dp[N]*dp[M-N]))
