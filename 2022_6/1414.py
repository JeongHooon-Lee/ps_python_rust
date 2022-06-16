import heapq
import sys

N = int(input())
edges: list = []
res = 0
total = 0
parents = {i: i for i in range(N)}

for i in range(N):
    data = list("".join(sys.stdin.readline().strip()))
    for j in range(N):
        if data[j] == "0":
            continue

        if ord(data[j]) > 96:
            temp = ord(data[j])-96
        else:
            temp = ord(data[j])-38
        total += temp

        if i != j:
            heapq.heappush(edges, (temp, i, j))


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while edges:
    value, start, depart = heapq.heappop(edges)
    start_parents = find_parents(start)
    depart_parents = find_parents(depart)

    if start_parents != depart_parents:
        parents[start_parents] = parents[depart_parents] = min(
            start_parents, depart_parents)
        res += value

res_check = set([find_parents(i) for i in range(N)])
if len(res_check) != 1:
    print(-1)
else:
    print(total - res)
