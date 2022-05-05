import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

left = data[:N//2]
right = data[N//2:]
left_part: list = []
right_part: list = []
for i in range(len(left)+1):
    for j in combinations(left, i):
        left_part.append(sum(j))
for i in range(len(right)+1):
    for j in combinations(right, i):
        right_part.append(sum(j))
left_part.sort()
right_part.sort(reverse=True)

len_of_left = len(left_part)
len_of_right = len(right_part)
res = p1 = p2 = 0

while p1 < len_of_left and p2 < len_of_right:
    if left_part[p1] + right_part[p2] == S:
        temp1 = 1
        temp2 = 1
        p1 += 1
        p2 += 1
        while p1 < len_of_left and left_part[p1] == left_part[p1-1]:
            p1 += 1
            temp1 += 1
        while p2 < len_of_right and right_part[p2] == right_part[p2-1]:
            p2 += 1
            temp2 += 1
        res += temp1*temp2

    elif left_part[p1] + right_part[p2] < S:
        p1 += 1
    else:
        p2 += 1

if S == 0:
    res -= 1

print(res)
