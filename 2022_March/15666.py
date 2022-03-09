import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(list(set(arr)))
N = len(arr)
def func(nums, cnt):
    if cnt == M:
        print(*nums)
        return
    
    for i in range(N):
        if not nums:
            func(nums+[arr[i]],cnt+1)
        else:
            if nums[-1] <= arr[i]:
                func(nums+[arr[i]],cnt+1)

func([],0)