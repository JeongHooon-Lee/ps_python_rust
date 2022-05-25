import heapq
import sys


def dijkstra(start: int):
    distances = {node: int(1e9) for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances


for _ in range(int(input())):
    N, M, T = map(int, sys.stdin.readline().split())
    S, G, H = map(int, sys.stdin.readline().split())
    depart = []
    res = []
    graph: dict = {}
    for i in range(N+1):
        graph[i] = {}
    for i in range(M):
        A, B, D = map(int, sys.stdin.readline().split())
        graph[A][B] = D
        graph[B][A] = D
    from_S = dijkstra(S)
    for i in range(T):
        from_G = dijkstra(G)
        from_H = dijkstra(H)
        TC = int(sys.stdin.readline().strip())
        # S->G->H->TC, S->H->G->TC
        if min(from_S[G] + from_G[H] + from_H[TC], from_S[H] + from_H[G] + from_G[TC]) == from_S[TC]:
            res.append(TC)
    res.sort()
    print(*res)
