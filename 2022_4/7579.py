import sys

N, M = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
res = sum(c)

dp = [ [0]*(res+1) for _ in range(N+1) ]


for i in range(1,N+1):
    weight = memory[i-1]
    value = c[i-1]
    for j in range(1,sum(c)+1):
        if j < value:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-value]+weight )
            
        if dp[i][j] >= M:
            res = min(res, j)

print(res)
