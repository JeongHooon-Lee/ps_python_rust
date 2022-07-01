import math
import sys


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while True:
    N = int(input())
    if N == 0:
        break
    pos: list = []
    edges: list = []
    parents = {i: i for i in range(N)}
    res = 0
    for i in range(N):
        pos.append(list(map(int, sys.stdin.readline().split())))

    for i in range(N-1):
        for j in range(i+1, N):
            value = math.sqrt((pos[i][0] - pos[j][0]) **
                              2 + (pos[i][1] - pos[j][1])**2)
            edges.append((value, i, j))

    for value, depart, desti in sorted(edges):
        depart_parents = find_parents(depart)
        desti_parents = find_parents(desti)
        if depart_parents != desti_parents:
            parents[depart_parents] = parents[desti_parents] = min(
                depart_parents, desti_parents)
            res += value
    print("{:.2f}".format(res))
