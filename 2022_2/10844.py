import sys

N = int(sys.stdin.readline().strip())
dp = [ [0] * 10 for _ in range(100) ]
dp[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,N):
    dp[i][0] = dp[i-1][1]
    dp[i][-1] = dp[i-1][-2]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[N-1])%1000000000)