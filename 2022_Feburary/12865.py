import sys

N, K = map(int, sys.stdin.readline().split())
data = []
dp = [ [0]*(K+1) for _ in range(N+1) ]

for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        weight = data[i-1][0]
        value = data[i-1][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value )

print(dp[N][K])