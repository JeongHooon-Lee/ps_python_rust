import sys

L1 = list(map(int, sys.stdin.readline().split()))
L2 = list(map(int, sys.stdin.readline().split()))


def ccw(A, B, C):
    res: int = 0
    res = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])
    if res < 0:  # 시계방향
        return -1
    elif res > 0:  # 빈시계방향
        return 1
    else:
        return 0


ccw123 = ccw([L1[0], L1[1]], [L1[2], L1[3]], [L2[0], L2[1]])
ccw124 = ccw([L1[0], L1[1]], [L1[2], L1[3]], [L2[2], L2[3]])
ccw341 = ccw([L2[0], L2[1]], [L2[2], L2[3]], [L1[0], L1[1]])
ccw342 = ccw([L2[0], L2[1]], [L2[2], L2[3]], [L1[2], L1[3]])
result = 0
if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
    result = 1
    if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
        if min(L1[0], L1[2]) <= max(L2[0], L2[2]) and min(L2[0], L2[2]) <= max(L1[0], L1[2]) and min(L1[1], L1[3]) <= max(L2[1], L2[3]) and min(L2[1], L2[3]) <= max(L1[1], L1[3]):
            result = 1
        else:
            result = 0
print(result)
