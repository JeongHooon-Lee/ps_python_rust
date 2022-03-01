import sys

N = int(input())

dp = [ 1 for _ in range(10) ]
for i in range(1,N+1):
    for j in range(1,10):
        dp[j] = (dp[j]%10007+dp[j-1]%10007)%10007
print(dp[-1])