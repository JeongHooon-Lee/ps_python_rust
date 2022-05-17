import sys

N, M = map(int, sys.stdin.readline().split())
matrix: list = []
visited = [[False]*M for _ in range(N)]
res = 0

for i in range(N):
    matrix.append(list("".join(sys.stdin.readline().strip())))


def counter(c):
    if c == "L":
        return "R"
    elif c == "R":
        return "L"
    elif c == "D":
        return "U"
    else:
        return "D"


def dfs(y, x):
    global res

    if visited[y][x]:
        return
    route.append((y, x))

    if matrix[y][x] == "D":
        visited[y][x] = True
        ny, nx = y+1, x
    elif matrix[y][x] == "U":
        visited[y][x] = True
        ny, nx = y-1, x
    elif matrix[y][x] == "R":
        visited[y][x] = True
        ny, nx = y, x+1
    else:
        visited[y][x] = True
        ny, nx = y, x-1

    if visited[ny][nx]:

        if matrix[ny][nx] == counter(matrix[y][x]):
            matrix[y][x] = "*"
            res += 1
        elif (ny, nx) in route:
            res += 1
        return
    else:
        dfs(ny, nx)


for i in range(N):
    for j in range(M):
        route: list = []
        dfs(i, j)

print(res)
