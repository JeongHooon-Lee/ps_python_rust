import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
matrix: list = []
for i in range(N):
    matrix.append(list("".join(sys.stdin.readline().strip())))


def solution(pos1: int, pos2: int) -> int:
    queue = deque()
    wall: dict = {}
    res = 1

    visited[pos1][pos2] = True
    deque.append(queue, (pos1, pos2))

    while queue:
        y, x = deque.popleft(queue)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if matrix[ny][nx] == "0" and visited[ny][nx] == False:
                    deque.append(queue, (ny, nx))
                    visited[ny][nx] = True
                    res += 1
                elif matrix[ny][nx] != "0":
                    try:
                        wall[(ny, nx)] = 1
                    except:
                        wall[(ny, nx)] = 1

    for nyy, nxx in wall.keys():
        matrix[nyy][nxx] = (int(matrix[nyy][nxx]) + res) % 10


visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == "0" and visited[i][j] == False:
            solution(i, j)


for i in matrix:
    print("".join(map(str, i)))
