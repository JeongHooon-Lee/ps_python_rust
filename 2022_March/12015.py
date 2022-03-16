import sys

N = int(input())
res = [0]
arr = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if arr[i] > res[-1]:
        res.append(arr[i])
    else:
        start = 0
        end = len(res)

        while start < end:
            mid = (start+end)//2
            if res[mid] <  arr[i]:
                start = mid+1
            else:
                end = mid
        res[end] = arr[i]
print(len(res)-1)