import sys

N = int(input())
edges: list = []
parents = {i: i for i in range(N)}
graph = [[] for i in range(N)]
for i in range(N-1):  # 0~4
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(N-i-1):  # 1~4 , 2~4
        edges.append((data[j], i, j+i+1))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


edges.sort()
for value, depart, desti in edges:
    depart_prts = find_parents(depart)
    desti_prts = find_parents(desti)
    if depart_prts != desti_prts:
        parents[depart_prts] = parents[desti_prts] = min(
            depart_prts, desti_prts)
        graph[depart].append(desti+1)
        graph[desti].append(depart+1)


for i in range(N):
    print(len(graph[i]), *sorted(graph[i]))
