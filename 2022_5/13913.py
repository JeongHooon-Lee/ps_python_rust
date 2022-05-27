import sys
from collections import deque

maxsize = 100000
N, K = map(int, sys.stdin.readline().split())
visited = [0]*(maxsize+1)
move_record = [0] * (maxsize+1)


def track(v: int, cnt: int) -> list[int]:
    res = [v]
    for _ in range(cnt):
        v = move_record[v]
        res.append(v)
    res.reverse()
    return res


def bfs():
    queue = deque()
    queue.append(N)

    while queue:
        v = queue.popleft()
        if v == K:
            break

        for nv in [v - 1, v + 1, v*2]:
            if 0 <= nv <= maxsize and visited[nv] == 0:
                visited[nv] = visited[v] + 1
                queue.append(nv)
                move_record[nv] = v
    cnt = visited[v]
    print(cnt)
    print(*track(K, cnt))


bfs()
