import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
datas = list(sys.stdin.readline().strip().split())
left_list: list = []
right_list: list = []
res: list = []
for char in datas:
    if char in ['a', 'e', 'i', 'o', 'u']:
        left_list.append(char)
    else:
        right_list.append(char)


for i in range(1, L-1):
    A = list(combinations(left_list, i))
    B = list(combinations(right_list, L-i))
    for j in A:
        for k in B:
            res.append("".join(sorted(j+k)))
for i in sorted(res):
    print(i)
