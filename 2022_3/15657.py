import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

def func(arr, cnt):
    if cnt == M:
        print(*arr)
        return
    
    for i in range(N):
        if not arr:
            func(arr+[num[i]],cnt+1)
        else:
            if num[i] >= arr[-1]:
                func(arr+[num[i]],cnt+1)
func([],0)
