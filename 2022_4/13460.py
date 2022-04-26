import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
matrix: list = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(N):
    matrix.append(list("".join(sys.stdin.readline().strip())))

for i in range(N):
    for j in range(M):
        if matrix[i][j] == "R":
            srx, sry = i, j
        if matrix[i][j] == "B":
            sbx, sby = i, j
        if matrix[i][j] == "O":
            ox, oy = i, j


def move(x, y, dx, dy):
    cnt = 0
    nx, ny = x, y
    while matrix[nx+dx][ny+dy] != '#' and matrix[nx][ny] != 'O':
        nx += dx
        ny += dy
        cnt += 1
    return nx, ny, cnt


def bfs():
    queue = deque()
    queue.append([srx, sry, sbx, sby, 0])
    visited = {}
    visited[(srx, sry)] = 1

    while queue:
        rx, ry, bx, by, cnt = queue.popleft()
        if cnt >= 10:
            return -1

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if matrix[nbx][nby] != 'O':
                if nrx == ox and nry == oy:
                    return cnt + 1
                # 같은위치일때
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx, nry = nrx-dx[i], nry-dy[i]
                    else:
                        nbx, nby = nbx-dx[i], nby-dy[i]
                if (nrx, nry, nbx, nby) in visited:
                    continue
                else:
                    visited[(nrx, nry, nbx, nby)] = 1
                    queue.append([nrx, nry, nbx, nby, cnt+1])
    return -1


print(bfs())
