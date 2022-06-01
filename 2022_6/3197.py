import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
visited = [[False] * C for _ in range(R)]
visited2 = [[False] * C for _ in range(R)]
swan_queue, swan_queue_next = deque(), deque()
water_queue, water_queue_next = deque(), deque()
matrix: list = []
swan_pos: list = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
res = 0


for i in range(R):
    input_ = list("".join(sys.stdin.readline().strip()))
    for j, k in enumerate(input_):
        if input_[j] == "L":
            swan_pos.append([i, j])
            water_queue.append((i, j))
        elif input_[j] == ".":
            visited[i][j] = True
            water_queue.append((i, j))
    matrix.append(input_)

swan_queue.append((swan_pos[0][0], swan_pos[0][1]))
matrix[swan_pos[0][0]][swan_pos[0][1]
                       ] = matrix[swan_pos[1][0]][swan_pos[1][1]] = "."
visited2[swan_pos[0][0]][swan_pos[0][1]] = True


def melt():
    while water_queue:
        y, x = water_queue.popleft()
        if matrix[y][x] == "X":
            matrix[y][x] = "."
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                if matrix[ny][nx] == "X":
                    water_queue_next.append((ny, nx))
                else:
                    water_queue.append((ny, nx))
                visited[ny][nx] = True

# swan visited2 = c
# else wc


def find_swan():
    while swan_queue:
        y, x = swan_queue.popleft()
        if y == swan_pos[1][0] and x == swan_pos[1][1]:
            return False
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and not visited2[ny][nx]:
                if matrix[ny][nx] == ".":
                    swan_queue.append((ny, nx))
                else:
                    swan_queue_next.append((ny, nx))
                visited2[ny][nx] = True
    return True


while True:
    melt()
    if not find_swan():
        break
    swan_queue, water_queue = swan_queue_next, water_queue_next
    swan_queue_next, water_queue_next = deque(), deque()
    res += 1
print(res)
