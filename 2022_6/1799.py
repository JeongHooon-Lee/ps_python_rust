import copy
import heapq
import sys

N = int(input())
matrix: list = []
spaces: list = []
heap: list = []

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if data[j] == 1:
            spaces.append((i, j))
    matrix.append(data)

length = len(spaces)


def check(y: int, x: int) -> bool:
    luy = ruy = ldy = rdy = y
    lux = rux = ldx = rdx = x
    while 0 <= luy and 0 <= lux:
        if matrix[luy][lux] == 2:
            return False
        luy -= 1
        lux -= 1
    while 0 <= ruy and rux < N:
        if matrix[ruy][rux] == 2:
            return False
        ruy -= 1
        rux += 1
    while ldy < N and 0 <= ldx:
        if matrix[ldy][ldx] == 2:
            return False
        ldy += 1
        ldx -= 1
    while rdy < N and rdx < N:
        if matrix[rdy][rdx] == 2:
            return False
        rdy += 1
        rdx += 1
    return True


def solution():
    res = 0

    while heap:
        value, y, x = heapq.heappop(heap)

        if check(y, x):
            matrix[y][x] = 2
            res += 1
    return res


def check2(y: int, x: int) -> int:
    luy = ruy = ldy = rdy = y
    lux = rux = ldx = rdx = x
    res = -4
    while 0 <= luy and 0 <= lux:
        if matrix[luy][lux] == 1:
            res += 1
        luy -= 1
        lux -= 1
    while 0 <= ruy and rux < N:
        if matrix[ruy][rux] == 1:
            res += 1
        ruy -= 1
        rux += 1
    while ldy < N and 0 <= ldx:
        if matrix[ldy][ldx] == 1:
            res += 1
        ldy += 1
        ldx -= 1
    while rdy < N and rdx < N:
        if matrix[rdy][rdx] == 1:
            res += 1
        rdy += 1
        rdx += 1
    return res


for y, x in spaces:
    heapq.heappush(heap, (check2(y, x), y, x))
print(solution())
