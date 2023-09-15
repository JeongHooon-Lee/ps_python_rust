import sys

R, C, K = map(int, sys.stdin.readline().split())
check_list = []
circulator_list = []
block_list = []

for i in range(R):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(C):
        if line[j] == 5:
            check_list.append((i, j))
        elif 0 < line[j] < 5:
            circulator_list.append((i, j, line[j]))

W = int(sys.stdin.readline())
for i in range(W):
    x, y, t = map(int, sys.stdin.readline().split())
    block_list.append((x - 1, y - 1, t))


def rotate_arr(arr: list[int]):
    new_r = len(arr[0])
    new_c = len(arr)
    new_arr = [[0 for _ in range(new_c)] for _ in range(new_r)]

    for i in range(new_c):
        for j in range(new_r):
            new_arr[j][new_c-i - 1] = arr[i][j]
    return new_arr


def rotate(R, C, r, c):
    return (C, R, c, R-1-r)


rotate_times = {1: 0, 2: 2, 3: 1, 4: 3}


def rotation_block_list(R, list):
    new_block_list = []
    for x, y, state in list:
        if state == 0:
            new_block_list.append((y, R-1-x, 1))
        else:  # 1
            new_block_list.append((y + 1, R-1 - x, 0))
    return new_block_list


def airshot(arr: list[int]):
    for r, c, direction in circulator_list:
        new_R, new_C = R, C
        new_block_list = block_list
        for _ in range(rotate_times[direction]):
            new_block_list = rotation_block_list(new_R, new_block_list)
            new_R, new_C, r, c = rotate(new_R, new_C, r, c)

        new_arr = [[0 for _ in range(new_C)] for _ in range(new_R)]
        count = 5
        new_arr[r][c+1] = count
        for i in range(c+1, c+6):
            count -= 1
            if i == new_C:
                break
            for j in range(new_R):
                if new_arr[j][i] > 1:
                    # 옆칸, 한칸위
                    if (j, i, 0) not in new_block_list and (j - 1, i, 1) not in new_block_list and 0 <= j - 1 and i + 1 < new_C:
                        new_arr[j - 1][i + 1] = count

                    # 바로 옆
                    if (j, i, 1) not in new_block_list and i + 1 < new_C:
                        new_arr[j][i + 1] = count

                    # 옆칸 바로 아래
                    if (j + 1, i, 0) not in new_block_list and (j + 1, i, 1) not in new_block_list and j + 1 < new_R and i + 1 < new_C:
                        new_arr[j + 1][i + 1] = count

        for _ in range((4 - rotate_times[direction]) % 4):
            new_arr = rotate_arr(new_arr)

        for i in range(R):
            for j in range(C):
                arr[i][j] += new_arr[i][j]
    return arr


def compare(a, b):
    return -((a - b) // 4) if a >= b else (b - a) // 4


def regulation(arr: list[int]):
    new_arr = [row[:] for row in arr]
    for i in range(R):
        for j in range(C):
            if j + 1 < C and (i, j, 1) not in block_list:
                comp = compare(arr[i][j], arr[i][j + 1])
                new_arr[i][j] += comp
                new_arr[i][j + 1] -= comp

            # 아래
            if i + 1 < R and (i + 1, j, 0) not in block_list:
                comp = compare(arr[i][j], arr[i + 1][j])
                new_arr[i][j] += comp
                new_arr[i + 1][j] -= comp
    return new_arr


def decrease(arr: list[int]):
    for i in range(R):
        if arr[i][0] >= 1:
            arr[i][0] -= 1
        if arr[i][C - 1] >= 1:
            arr[i][C - 1] -= 1

    for i in range(1, C - 1):
        if arr[0][i] >= 1:
            arr[0][i] -= 1
        if arr[R - 1][i] >= 1:
            arr[R - 1][i] -= 1
    return arr


def check_end(arr: list[int]):
    for r, c in check_list:
        if arr[r][c] < K:
            return False
    return True


arr = [[0 for _ in range(C)] for _ in range(R)]
result = 0
while not check_end(arr) and result <= 101:
    arr = airshot(arr)
    arr = regulation(arr)
    arr = decrease(arr)
    result += 1


print(result if result <= 100 else 101)
