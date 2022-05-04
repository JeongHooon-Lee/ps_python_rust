# 너무 어렵다 이문제
import sys

N = int(input())
matrix: list = []
dp = [[sys.maxsize] * (1 << N) for _ in range(N)]

for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))


def dfs(x, visited):
    if visited == (1 << N) - 1:
        if matrix[x][0]:
            return matrix[x][0]
        else:
            return sys.maxsize
    if dp[x][visited] != sys.maxsize:
        return dp[x][visited]

    for i in range(1, N):
        # 길이 없으면
        if not matrix[x][i]:
            continue

        # 지금 가려는 곳이 이미 방문한곳이면
        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited],
                             dfs(i, visited | (1 << i)) + matrix[x][i])
    return dp[x][visited]


print(dfs(0, 1))
