import sys

N, M = map(int, sys.stdin.readline().split())
edges: list = []
parents = {i: i for i in range(N+1)}
res = 0
for i in range(M):
    pos, value = map(int, sys.stdin.readline().split())
    edges.append((value, 0, pos))
costs = list(map(int, sys.stdin.readline().split()))

for i in range(1, N+1):
    temp = i+1 if i != N else 1
    edges.append((costs[i-1], i, temp))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for value, depart, desti in sorted(edges):
    depart_parents = find_parents(depart)
    desti_parents = find_parents(desti)
    if depart_parents != desti_parents:
        parents[depart_parents] = parents[desti_parents] = min(
            depart_parents, desti_parents)
        res += value
print(res)
