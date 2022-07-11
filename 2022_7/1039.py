import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque()
queue.append((N, 0))
res = -1
length = len(str(N))
is_exist = set()

while queue:
    current, count = queue.popleft()
    if count == K:
        res = max(res, current)
        continue
    else:
        for i in range(length-1):
            for j in range(i+1, length):
                temp_current = list(str(current))
                if i == 0 and temp_current[j] == "0":
                    continue
                temp_current[i], temp_current[j] = temp_current[j], temp_current[i]
                next_ = int("".join(temp_current))
                if (next_, count+1) not in is_exist:
                    queue.append((next_, count+1))
                    is_exist.add((next_, count+1))

print(res)
