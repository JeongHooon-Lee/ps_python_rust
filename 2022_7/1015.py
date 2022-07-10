import re
import sys

N = int(input())
datas = list(map(int, sys.stdin.readline().split()))
res: list = [0]*N
temp_array = sorted(enumerate(datas), key=lambda x: x[1])
for i in range(N):
    res[temp_array[i][0]] = i
print(*res)
