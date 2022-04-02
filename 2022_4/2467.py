import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

left = 0 
right = N-1

res = [arr[left], arr[right]]

while left < right:
    if abs(res[0] + res[1]) == 0:
        break
    
    if abs(res[1] + res[0]) > abs(arr[right] + arr[left]):
        res = [arr[left], arr[right]]
    
    if arr[left] + arr[right] < 0:
        left+=1
    elif arr[left] + arr[right] > 0:
        right-=1
    
print(*res)