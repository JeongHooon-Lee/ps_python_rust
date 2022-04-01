import sys
import heapq
N, K = map(int, sys.stdin.readline().split())
gem = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(gem, (M,V))

storage_of_bag = []
for _ in range(K):
    storage_of_bag.append(int(input()))
storage_of_bag.sort()

res = 0
can_in = []
for bag in storage_of_bag:
    while gem and bag >= gem[0][0]:
        heapq.heappush(can_in, -heapq.heappop(gem)[1])
    if can_in:
        res -= heapq.heappop(can_in)
    else:
        continue
print(res)
# pypy