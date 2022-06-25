import sys


def find_parents(v: int, parents: dict) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v], parents)
    return parents[v]


def min_count(list1, list2):
    parents = {i: i for i in range(N+1)}
    res = 0
    for edges, cost in ((list1, 0), (list2, 1)):
        for depart, desti in edges:
            depart_parnets = find_parents(depart, parents)
            desti_parnets = find_parents(desti, parents)
            if depart_parnets != desti_parnets:
                parents[depart_parnets] = parents[desti_parnets] = min(
                    depart_parnets, desti_parnets)
                res += cost
    return res


while True:
    N, M, K = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0 and K == 0:
        break
    blue_edges: list = []
    red_edges: list = []
    for i in range(M):
        C, F, T = sys.stdin.readline().strip().split()
        F, T = map(int, (F, T))
        if C == 'B':
            blue_edges.append((F, T))
        else:
            red_edges.append((F, T))

    min_blue_count = min_count(red_edges, blue_edges)
    min_red_count = min_count(blue_edges, red_edges)
    max_blue_count = N - min_red_count - 1
    if min_blue_count <= K <= max_blue_count:
        print(1)
    else:
        print(0)
