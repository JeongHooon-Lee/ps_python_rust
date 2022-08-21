import sys
from itertools import combinations

n, m, k = map(int, sys.stdin.readline().split())
res = 0
ll = [*combinations([i for i in range(n)], m)]
for i in ll:
    count = 0
    for j in range(m):
        if i[j] < m:
            count += 1
    if count >= k:
        res += 1
print(res/len(ll))
