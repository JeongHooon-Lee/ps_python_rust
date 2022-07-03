import sys
from collections import deque

N, M, S = map(int, sys.stdin.readline().split())
matrix: list = []
for i in range(N):
    matrix.append(list("".join(sys.stdin.readline().split())))
names = sys.stdin.readline().strip()
alpha: dict = {}
alpha = {chr(i): deque() for i in range(97, 123)}
res = []
for i in range(N):
    for j in range(M):
        alpha[matrix[i][j]].append([i, j])
c = sys.maxsize
for i in range(S):
    t = names.count(names[i])
    c = min(c, len(alpha[names[i]]) // t)

current_x = 0
current_y = 0
target_inx = 0


def solution(cx, cy, tx, ty):
    global res
    temp_y = abs(ty-cy)
    temp_x = abs(tx-cx)
    if cy < ty:
        res += ["D"]*temp_y
    else:
        res += ["U"]*temp_y
    if cx < tx:
        res += ["R"]*temp_x
    else:
        res += ["L"]*temp_x
    res += ["P"]
    return tx, ty


for _ in range(c*S):
    target = alpha[names[target_inx]]
    target_y, target_x = target.popleft()
    current_x, current_y = solution(current_x, current_y, target_x, target_y)
    target_inx = (target_inx+1) % S

res += ["R"]*(M-current_x-1)
res += ["D"]*(N-current_y-1)
print(c, len(res))
print("".join(res))
