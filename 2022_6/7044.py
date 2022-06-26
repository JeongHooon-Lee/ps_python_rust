import sys

N, M = map(int, sys.stdin.readline().split())
parents = {i: i for i in range(N+1)}
edges: list = []
res = 0
for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((C, A, B))
edges.sort(reverse=True)


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for value, depart, desti in edges:
    depart_parents = find_parents(depart)
    desit_parents = find_parents(desti)
    if depart_parents != desit_parents:
        parents[depart_parents] = parents[desit_parents] = min(
            depart_parents, desit_parents)
        res += value

test = set(list(find_parents(i) for i in range(1, N+1)))
if len(test) == 1:
    print(res)
else:
    print(-1)
