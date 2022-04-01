import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def func(a, b): 
    minnum = min(a,b)
    if minnum == 1:
        return a, b
    for i in range(minnum,1,-1):
        if a%i == 0 and b%i == 0:
            return func(a//i, b//i)
    return a, b

for i in range(1,N):
    x,y = func(arr[0],arr[i])
    print("%d/%d" %(x,y))