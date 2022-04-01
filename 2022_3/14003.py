import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
LIS = []
record = [0]*N

def binary_search(target):
    left = 0
    right = len(LIS)
    while left < right:
        mid = (left + right) // 2
        if LIS[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

for i in range(len(array)):
    if not LIS or LIS[-1] < array[i]:
        record[i] = len(LIS)
        LIS.append(array[i])
    else:
        input_index = binary_search(array[i])
        record[i] = input_index
        LIS[input_index] = array[i]

len_of_LIS = len(LIS)
print(len_of_LIS)
res = []
for i in range(N-1,-1,-1):
    if record[i] == len_of_LIS - 1:
        res.append(array[i])
        len_of_LIS -= 1
res.sort()
print(*res)
