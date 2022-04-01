import sys

def func(a,b):
    global temp
    if a <= 0 and b <= 0:
        return 
    for i in range(2,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            temp.append(i)
            return func(a//i,b//i)
    if a != b:
        temp.append(a)
    temp.append(b)

t = int(input())
for i in range(t):
    a, b= list(map(int, sys.stdin.readline().split()))
    temp = []
    func(a,b)
    answer = 1
    for i in temp:
        answer*=i
    print(answer)