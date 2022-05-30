import sys

sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N+1)]


def find_parents(v):
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


def union(v1, v2):
    v1_parents = find_parents(v1)
    v2_parents = find_parents(v2)
    if v1_parents != v2_parents:
        parents[v1_parents] = parents[v2_parents] = min(v1_parents, v2_parents)


for i in range(M):
    operator, a, b = map(int, sys.stdin.readline().split())

    if operator == 0:
        union(a, b)
    elif operator == 1:
        if find_parents(a) == find_parents(b):
            print("YES")
        else:
            print("NO")
