import sys
n, k = map(int, sys.stdin.readline().split())
arr : list = []
dp = [ 0 for _ in range(k+1) ]
dp[0] = 1

for i in range(n):
    arr.append(int(input()))

for i in arr:
    for j in range(1,k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
print(dp[-1])