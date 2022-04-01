import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

for i in range(1,len(arr)):
    arr[i] = arr[i]+arr[i-1]

print(sum(arr))