import sys

N = int(input())
array : list = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    array.append((a,b))
array.sort(key = lambda x : x[0])
LIS = []

def binary_search(target):
    left = 0
    right = len(LIS)-1
    while left < right:
        mid = (left+right)//2
        if LIS[mid] < target:
            left = mid +1
        else:
            right = mid
    return 
    
store_index = []
for i in array:
    if not LIS:
        LIS.append(i[1])
        store_index.append(0)
    elif LIS[-1] < i[1]:
        LIS.append(i[1])
        store_index.append(len(LIS)-1)
    else:
        target_index = binary_search(i[1])
        LIS[target_index] = i[1]
        store_index.append(target_index)

len_of_LIS = len(LIS) - 1
need_cut = []
for i in range(N-1,-1,-1):
    if store_index[i] == len_of_LIS:
        len_of_LIS -= 1
    else: 
        need_cut.append(i)
print(len(need_cut))
for _ in range(len(need_cut)):
    print(array[need_cut.pop()][0])
