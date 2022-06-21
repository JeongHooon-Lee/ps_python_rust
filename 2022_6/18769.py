import sys

T = int(sys.stdin.readline().strip())


def find_parents(v: int) -> int:
    if v != parents[v]:
        parents[v] = find_parents(parents[v])
    return parents[v]


for _ in range(T):
    R, C = map(int, sys.stdin.readline().split())
    edges: list = []
    res = 0
    parents = {i: i for i in range(R*C)}
    for i in range(R):
        input_data = list(map(int, sys.stdin.readline().split()))
        for j in range(C-1):
            edges.append((input_data[j], C*i+j, C*i+j+1))

    for i in range(R-1):
        input_data = list(map(int, sys.stdin.readline().split()))
        for j in range(C):
            edges.append((input_data[j], C*i+j, C*(i+1)+j))

    edges.sort()
    for edge in edges:
        value, start, depart = edge
        start_parents = find_parents(start)
        depart_parents = find_parents(depart)
        if start_parents != depart_parents:
            parents[start_parents] = parents[depart_parents] = min(
                start_parents, depart_parents)
            res += value

    sys.stdout.write(str(res)+"\n")
