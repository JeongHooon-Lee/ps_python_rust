import sys
from collections import deque
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())
queue = deque()
queue.append(N)
res = -1
length = len(str(N))
datas = [i for i in range(length)]
trader = list(combinations(datas, 2))


def bfs():
    is_exist = set()
    ans = 0
    queue_len = len(queue)
    while queue_len:
        current = queue.popleft()
        for i, j in trader:
            temp_current = list(str(current))
            temp_current[i], temp_current[j] = temp_current[j], temp_current[i]
            if temp_current[0] == "0":
                continue
            next_ = int("".join(temp_current))
            if next_ not in is_exist:
                ans = max(ans, next_)
                queue.append(next_)
                is_exist.add(next_)
        queue_len -= 1
    return ans


while K:
    res = bfs()
    K -= 1
print(res)
