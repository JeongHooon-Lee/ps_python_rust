import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
def func(num, cnt):
    if cnt == M:
        print(*num)
        return
    
    for i in range(N):
        if not num:
            func(num+[arr[i]],cnt+1)
        else:
            if arr[i] not in num:
                func(num+[arr[i]],cnt+1)
func([],0)