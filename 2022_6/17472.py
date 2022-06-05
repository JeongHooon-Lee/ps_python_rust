import heapq
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
edges = []
visited = [[False]*M for _ in range(N)]
islands: list = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
matrix: list = []
cnt = 1
res = 0


def dfs(y: int, x: int) -> list[int]:
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True
    matrix[y][x] = cnt
    box_index = [(y, x)]

    while queue:
        ty, tx = queue.popleft()
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and matrix[ny][nx] == 1:
                visited[ny][nx] = True
                matrix[ny][nx] = cnt
                queue.append((ny, nx))
                box_index.append((ny, nx))

    return box_index


for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            islands.append(dfs(i, j))
            cnt += 1

num_of_islands = len(islands)
for i in range(num_of_islands):
    for y, x in islands[i]:
        for k in [[-1, 0], [0, -1]]:
            ty = y
            tx = x
            count = 0
            while True:
                ty -= k[0]
                tx -= k[1]
                if 0 <= ty < N and 0 <= tx < M:
                    if matrix[ty][tx] == i+1:
                        break
                    if matrix[ty][tx] == 0:
                        count += 1
                    elif matrix[ty][tx] != i+1 and matrix[ty][tx] > 0:
                        if count > 1:
                            heapq.heappush(edges, (count, i, matrix[ty][tx]-1))
                        break
                else:
                    break

parents = {i: i for i in range(num_of_islands)}


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while edges:
    distance, v1, v2 = heapq.heappop(edges)
    parents_v1 = find_parents(v1)
    parents_v2 = find_parents(v2)
    if parents_v1 != parents_v2:
        res += distance
        parents[parents_v1] = parents[parents_v2] = min(parents_v1, parents_v2)

res_parents = set([find_parents(v) for v in range(num_of_islands)])

if len(res_parents) != 1 or res == 0:
    print(-1)
else:
    print(res)
