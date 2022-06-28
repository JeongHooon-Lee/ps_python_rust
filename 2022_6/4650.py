import sys


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


while True:
    N = int(input())
    if N == 0:
        break
    edges: list = []
    parents = {chr(i): chr(i) for i in range(65, 65+N)}
    res = 0
    for i in range(N-1):
        input_ = list(sys.stdin.readline().strip().split())

        for j in range(int(input_[1])):
            edges.append((int(input_[3+j*2]), input_[0], input_[2+j*2]))

    edges.sort()

    for value, depart, desti in edges:
        depart_parents = find_parents(depart)
        desti_parents = find_parents(desti)
        if depart_parents != desti_parents:
            parents[depart_parents] = parents[desti_parents] = min(
                depart_parents, desti_parents)
            res += value
    print(res)
