import sys

N, M, R = map(int, sys.stdin.readline().split())
items = [0] + list(map(int, sys.stdin.readline().split()))
dp = [ [10001]*(N+1) for _ in range(N+1) ]

for i in range(R):
    a, b, i = map(int , sys.stdin.readline().split())
    dp[a][b] = i
    dp[b][a] = i
for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            dp[i][j] = 0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
# for i in dp:
#     print(*i)

res = 0
for i in range(1,N+1):
    sumnum = 0
    for j in range(1,N+1):
        if dp[i][j] <= M and dp[i][j] != 10001:
            sumnum += items[j]
    res = max(res, sumnum)
print(res)