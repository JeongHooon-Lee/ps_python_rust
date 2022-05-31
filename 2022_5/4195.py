import sys


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


def union(v1: int, v2: int) -> int:
    v1_parents = find_parents(v1)
    v2_parents = find_parents(v2)

    if v1_parents != v2_parents:
        min_parents = v1_parents if v1_parents < v2_parents else v2_parents
        max_parents = v2_parents if v1_parents < v2_parents else v1_parents

        parents[max_parents] = min_parents
        res[min_parents] += res[max_parents]
        res[max_parents] = 0
        return min_parents
    return v1_parents


for _ in range(int(input())):
    F = int(input())
    numeric: dict = {}
    parents: dict = {}
    res: dict = {}
    cnt = 0
    for i in range(F):
        f1, f2 = sys.stdin.readline().strip().split()
        for f3 in [f1, f2]:
            try:
                numeric[f3]
            except:
                numeric[f3] = cnt
                parents[cnt] = cnt
                res[cnt] = 1
                cnt += 1
        low = union(numeric[f1], numeric[f2])
        print(res[low])
