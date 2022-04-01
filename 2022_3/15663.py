import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = [False]*N
res = []
def func(nums, cnt):
    if cnt == M:
        print(*nums)  
        return 
    last = 0
    for i in range(N):
        if not visited[i] and last != arr[i]:
            visited[i] = True
            last = arr[i]
            func(nums+[arr[i]],cnt+1)
            visited[i] = False
func([],0)
