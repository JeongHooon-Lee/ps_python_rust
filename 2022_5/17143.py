import sys

R, C, M = map(int, sys.stdin.readline().split())
shark: dict = {}
alive = [True] * M
matrix = [[-1] * C for _ in range(R)]
human_pos = -1
res = 0
for i in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    matrix[r-1][c-1] = i
    shark[i] = [r-1, c-1, s, d, z]


def shark_move_vertical(now, speed, direction):
    for _ in range(speed):
        if direction == 1:  # 윗방향
            if now == 0:
                direction = 2
                now += 1
            else:
                now -= 1
        else:
            if now == R-1:
                direction = 1
                now -= 1
            else:
                now += 1
    return now, direction


def shark_move_horizon(now, speed, direction):
    for _ in range(speed):
        if direction == 4:
            if now == 0:
                direction = 3
                now += 1
            else:
                now -= 1
        else:
            if now == C-1:
                direction = 4
                now -= 1
            else:
                now += 1
    return now, direction


def shark_move():
    for i in range(M):
        if alive[i]:
            # 원래 있던 자리 초기화
            if matrix[shark[i][0]][shark[i][1]] == i:
                matrix[shark[i][0]][shark[i][1]] = -1

            if shark[i][3] == 1 or shark[i][3] == 2:  # 세로
                pos, direction = shark_move_vertical(
                    shark[i][0], shark[i][2], shark[i][3])
                shark[i][0] = pos
                shark[i][3] = direction
            else:  # 가로
                pos, direction = shark_move_horizon(
                    shark[i][1], shark[i][2], shark[i][3])
                shark[i][1] = pos
                shark[i][3] = direction

            target = matrix[shark[i][0]][shark[i][1]]

            # 이동한 자리에 아무것도 없으면
            if target == -1:
                matrix[shark[i][0]][shark[i][1]] = i
            # 이동한 자리에 아직 이동안한 상어가 있으면
            elif target != -1 and target > i:
                matrix[shark[i][0]][shark[i][1]] = i
            else:
                # 만약 이동한 위치에 상어가 있고 그 상어가 이동한 상태이며, 나보다 크기가 작다면
                if target != -1 and target < i and shark[target][-1] < shark[i][-1]:
                    matrix[shark[i][0]][shark[i][1]] = i
                    alive[target] = False
                # 나보다 크기가 크다면
                elif target != -1 and target < i and shark[target][-1] > shark[i][-1]:
                    alive[i] = False


def human_move(human_pos):
    for i in range(R):
        temp = matrix[i][human_pos]
        if temp != -1:
            alive[temp] = False
            matrix[i][human_pos] = -1
            return shark[temp][-1]
    return 0


for _ in range(C):
    human_pos += 1
    res += human_move(human_pos)
    shark_move()
print(res)
