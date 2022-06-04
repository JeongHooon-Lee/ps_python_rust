import heapq
import math
import sys

N, M = map(int, sys.stdin.readline().split())
parents = {i: i for i in range(N+1)}
pos = [(0, 0)]
queue: list = []
res = 0


def distance(v1: int, v2: int) -> int:
    return math.sqrt((pos[v1][0] - pos[v2][0])**2 + (pos[v1][1] - pos[v2][1])**2)


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())
    pos.append((X, Y))

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    X_parnets = find_parents(X)
    Y_parents = find_parents(Y)
    if X_parnets != Y_parents:
        parents[X_parnets] = parents[Y_parents] = min(X_parnets, Y_parents)


for i in range(1, N):
    for j in range(i+1, N+1):
        if find_parents(i) != find_parents(j):
            heapq.heappush(queue, (distance(i, j), i, j))

while queue:
    D, A, B = heapq.heappop(queue)
    A_parents = find_parents(A)
    B_parents = find_parents(B)
    if A_parents != B_parents:
        parents[A_parents] = parents[B_parents] = min(A_parents, B_parents)
        res += D
print(format(res, ".2f"))
