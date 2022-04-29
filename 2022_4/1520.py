import sys

sys.setrecursionlimit(10**6)
M, N = map(int, sys.stdin.readline().split())
matrix: list = []
for i in range(M):
    matrix.append(list(map(int, sys.stdin.readline().split())))

visited = [[-1]*N for _ in range(M)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1
    if visited[y][x] != -1:
        return visited[y][x]
    visited[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < M and 0 <= nx < N and matrix[ny][nx] < matrix[y][x]:
            visited[y][x] += dfs(ny, nx)
    return visited[y][x]


print(dfs(0, 0))
