import sys
N = int(input())
matrix : list = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

res = sys.maxsize
for i in range(3):
    dp = [[0]*3 for _ in range(N)]
    dp[0][0] = dp[0][1] = dp[0][2] = matrix[0][i]
    for j in range(3):
        if j == i:
            dp[1][i] = sys.maxsize
        else:
            dp[1][j] = matrix[0][i] + matrix[1][j]
    for j in range(2,N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + matrix[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + matrix[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + matrix[j][2]
    for j in range(3):
        if j == i:
            continue
        res = min(res , dp[N-1][j])
print(res)