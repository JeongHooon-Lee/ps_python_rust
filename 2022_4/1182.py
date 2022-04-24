import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

res = 0
for i in range(1, N+1):
    for j in combinations(nums, i):
        if sum(j) == S:
            res += 1
print(res)
