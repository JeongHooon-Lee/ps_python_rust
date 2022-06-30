import sys


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    parents = {i: i for i in range(N+1)}
    edges: list = []
    res: list = []
    for i in range(M):
        s, t, c = map(int, sys.stdin.readline().split())
        edges.append((c, s, t))
    edges.sort()

    for value, depart, desti in edges:
        parents_depart = find_parents(depart)
        parents_desti = find_parents(desti)
        if parents_depart != parents_desti:
            parents[parents_depart] = parents[parents_desti] = min(
                parents_desti, parents_depart)
            res.append(value)
    res.sort()
    if N == 2:
        print(res[0])
    else:
        print(res[(N-1)//2])
