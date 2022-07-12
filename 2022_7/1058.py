import copy
import sys
from itertools import combinations

N = int(input())
friends = {i: set() for i in range(N)}
res = [0]*N
for i in range(N):
    data = list("".join(sys.stdin.readline().split()))
    for j in range(i+1, N):
        if data[j] == 'Y':
            friends[i].add(j)
            friends[j].add(i)
    res = len(friends[i])
res = copy.deepcopy(friends)

for i in range(N):
    for j, k in list(combinations(friends[i], 2)):
        res[j].add(k)
        res[k].add(j)

res = max([len(res[i]) for i in range(N)])
print(res)
