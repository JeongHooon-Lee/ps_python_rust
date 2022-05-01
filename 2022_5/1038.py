import sys
from itertools import combinations

N = int(input())

list_of_num: list = []

for i in range(1, 11):
    for combination in combinations(range(0, 10), i):
        combination = list(combination)
        combination.sort(reverse=True)
        # print(combination)
        list_of_num.append(int("".join(map(str, combination))))
list_of_num.sort()

try:
    print(list_of_num[N])
except:
    print(-1)
