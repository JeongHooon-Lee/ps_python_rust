import sys

for _ in range(int(input())):
    N = int(input())
    data = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * (N) for _ in range(N)]

    for v in range(1, N):
        for i in range(N-v):
            j = i+v
            dp[i][j] = sys.maxsize
            s = sum(data[i:j+1])
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + s)
    print(dp[0][N-1])
