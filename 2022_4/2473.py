# pypy3
import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


res = [sys.maxsize]

for i in range(N-1):
    left = i+1
    right = N-1
    while left < right:
        if abs(sum(res)) == 0:
            break
        
        if abs(sum(res)) > abs(arr[i] + arr[right] + arr[left]):
            res = [arr[i], arr[left], arr[right]]
        
        if arr[i]+ arr[left] + arr[right] < 0:
            left+=1
        elif arr[i] + arr[left] + arr[right] > 0:
            right-=1
    
print(*res)