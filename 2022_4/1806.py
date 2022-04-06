import sys

N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
sum = numbers[0]
res = sys.maxsize

while 0 <= right < N:
    if sum < S:
        if right != N-1:
            right +=1
            sum+=numbers[right]
        else:
            break
    elif sum >= S:
        res = min(res, right-left+1)
        sum-=numbers[left]
        left +=1

if res == sys.maxsize:
    print(0)
else:    
    print(res)