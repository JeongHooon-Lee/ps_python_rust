import sys

N = int(input())
datas = list(map(int, sys.stdin.readline().split()))
record = [0] * N
lis: list = []
res: list = []


def binary(v: int) -> int:
    left = 0
    right = len(lis)
    while left < right:
        mid = (left+right)//2
        if lis[mid] < v:
            left = mid + 1
        else:
            right = mid
    return right


for i in range(N):
    if not lis or lis[-1] < datas[i]:
        record[i] = len(lis)
        lis.append(datas[i])
    else:
        idx = binary(datas[i])
        record[i] = idx
        lis[idx] = datas[i]

len_of_LIS = len(lis)
print(len_of_LIS)
for i in range(N-1, -1, -1):
    if record[i] == len_of_LIS - 1:
        res.append(datas[i])
        len_of_LIS -= 1
res.sort()
print(*res)
