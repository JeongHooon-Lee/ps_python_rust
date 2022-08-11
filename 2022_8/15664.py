import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
datas = list(map(int, sys.stdin.readline().split()))
res: list = []

for com in list(combinations(datas, M)):
    if sorted(com) not in res:
        res.append(sorted(com))

for i in sorted(res):
    print(*i)
