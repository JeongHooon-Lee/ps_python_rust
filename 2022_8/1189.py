import sys
from collections import deque

R, C, K = map(int, sys.stdin.readline().split())
matrix: list = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
res = 0
for i in range(R):
    matrix.append(list("".join(sys.stdin.readline().strip())))


def bfs():
    global res
    queue = deque()
    queue.append((0, R-1, 1, [(0, R-1)]))

    while queue:
        x, y, cnt, history = queue.popleft()

        if x == C-1 and y == 0 and cnt == K:
            res += 1
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < R and 0 <= nx < C and matrix[ny][nx] != 'T' and (nx, ny) not in history:
                if cnt < K:
                    queue.append((nx, ny, cnt+1, history+[(nx, ny)]))


bfs()
print(res)
