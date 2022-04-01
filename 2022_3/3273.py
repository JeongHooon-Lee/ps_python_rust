import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
X = int(input())

left= 0
right = N-1
res = 0
while left < right:
    temp = arr[left] + arr[right]
    if temp == X:
        res+=1
    if temp < X:
        left +=1
        continue
    right -=1
print(res)