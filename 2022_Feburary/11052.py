import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr = [0]+arr
dp = [0] * (N+1)
dp[1], dp[2] = arr[1], max(dp[1]*2,arr[2])

for i in range(3,N+1):
    dp[i] = max(dp[1]*i,arr[i])
    for j in range(1,(i//2)+1):
        dp[i] = max(dp[i],dp[j]+dp[i-j])
print(dp[-1])
# dp[1] = arr[1]
# dp[2] = arr[1]*2,arr[2]
# dp[3] = dp[1]*3 or arr[3] or arr[2]+arr[1]4
