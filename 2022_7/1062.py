import sys
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())
datas = []
# a, n, t ,i c
alpha = {}
cnt = 0
for i in range(97, 123):
    if chr(i) in "antic":
        continue
    alpha[chr(i)] = cnt
    cnt += 1
res = 0

for i in range(N):
    data = sys.stdin.readline().strip()
    datas.append(data)


def word_parse(data: str):
    res = 0
    for i in data:
        if i not in "antic":
            res |= 1 << alpha[i]
    return res


if K < 5:
    print(0)
    exit()

datas = list(map(word_parse, datas))
for i in list(combinations([i for i in range(21)], K-5)):
    temp_res = 0
    for data in datas:
        if data & sum([2**j for j in i]) == data:
            temp_res += 1
    res = max(res, temp_res)
print(res)
