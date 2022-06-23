import sys


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for _ in range(int(input())):
    matrix: list = []
    edges: list = []
    N = int(input())
    parents = {i: i for i in range(N)}
    res = 0
    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N-1):
        for j in range(i+1, N):
            if matrix[i][j] == 1:
                edges.append((1, i, j))
    edges.sort()

    for value, depart, destination in edges:
        depart_prts = find_parents(depart)
        desi_prts = find_parents(destination)
        if depart_prts != desi_prts:
            parents[desi_prts] = parents[depart_prts] = min(
                desi_prts, depart_prts)
            res += value
    print(res)
