import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]*N
dp[0] = 1
answer = 1
for i in range(1,N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)
    answer = max(dp[i], answer)
print(answer)