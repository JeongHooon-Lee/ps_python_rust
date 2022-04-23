import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())


def dfs(startY, startX):
    queue = deque()
    queue.append((startY, startX))
    visited = [[False] * w for _ in range(h)]
    visited[startY][startX] = True
    res = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and matrix[ny][nx] != "*":
                if matrix[ny][nx] == ".":
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                elif matrix[ny][nx] == "$":
                    res += 1
                    queue.append((ny, nx))
                    visited[ny][nx] = True
                else:
                    character = matrix[ny][nx]
                    if 97 <= ord(character) <= 122:  # 소문자일때
                        keys.append(ord(character))
                        visited = [[False] * w for _ in range(h)]
                        matrix[ny][nx] = "."
                        queue.append((ny, nx))
                        visited[ny][nx] = True
                    else:
                        # 대문자이고 키가 있으면
                        if chr(ord(character)+32) in keys:
                            matrix[ny][nx] = "."
                            queue.append((ny, nx))
                            visited[ny][nx] = True

    return res


for i in range(t):
    h, w = map(int, sys.stdin.readline().split())
    matrix: list = []
    keys: list = []
    for i in range(h):
        matrix.append(list("".join(sys.stdin.readline().strip())))
    keys += list("".join(sys.stdin.readline().strip()))
    print(dfs(1, 0))
