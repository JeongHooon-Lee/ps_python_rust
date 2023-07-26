import sys
from collections import deque


class Coordinate:
    def __init__(self, x=-1, y=-1):
        self.x, self.y = x, y


four_way = [[1, 0], [-1, 0], [0, 1], [0, -1]]

N, M = map(int, input().split())
coordi = Coordinate()
field = []


for i in range(N):
    line = list("".join(sys.stdin.readline().strip()))
    if coordi.x == -1 and 'I' in line:
        coordi.x, coordi.y = i, line.index('I')
    field.append(line)


def is_valid(x: int, y: int, field: list[list[chr]]) -> bool:
    return 0 <= x < N and 0 <= y < M and field[x][y] != 'X'


def bfs(coordinate: Coordinate, field: list[list[chr]]) -> int:
    queue = deque()
    queue.append(coordinate)
    visited = [[0]*M for _ in range(N)]
    visited[coordinate.x][coordinate.y] = 1
    result = 0

    while queue:
        current = queue.popleft()

        for i in range(4):
            next_x = current.x + four_way[i][0]
            next_y = current.y + four_way[i][1]
            if is_valid(next_x, next_y, field) and visited[next_x][next_y] != 1:
                if field[next_x][next_y] == 'P':
                    result += 1
                visited[next_x][next_y] = 1
                next_ = Coordinate(next_x, next_y)
                queue.append(next_)

    return result


answer = bfs(coordi, field)
print("TT" if answer == 0 else answer)
