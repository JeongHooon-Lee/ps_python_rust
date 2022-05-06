import copy
import sys

matrix: list = []
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

ans = 101
for i in range(10):
    temp = list("".join(sys.stdin.readline().strip()))
    for j in range(10):
        if temp[j] == "O":
            temp[j] = True
        else:
            temp[j] = False
    matrix.append(temp)

for i in range(1024):
    table = copy.deepcopy(matrix)
    cnt = 0

    for j in range(10):
        if i & (1 << j):
            cnt += 1
            for k in range(5):
                ny = 0 + dy[k]
                nx = j + dx[k]
                if 0 <= ny < 10 and 0 <= nx < 10:
                    table[ny][nx] = not table[ny][nx]

    for j in range(1, 10):
        for k in range(10):
            if table[j-1][k]:
                for l in range(5):
                    ny = j+dy[l]
                    nx = k+dx[l]
                    if 0 <= ny < 10 and 0 <= nx < 10:
                        table[ny][nx] = not table[ny][nx]

                cnt += 1

    temp = True
    for j in range(10):
        if table[9][j] == True:
            temp = False
    if temp:
        ans = min(ans, cnt)

print(ans if ans != 101 else -1)
