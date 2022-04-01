import sys

answer : dict = {}
N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
sorted_Array = sorted(list(set(array)))

for i in range(len(sorted_Array)):
    answer[sorted_Array[i]] = i

for i in array:
    print(answer[i], end=" ")