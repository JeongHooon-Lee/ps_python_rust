import sys

def func(a, b):
    if b == 1:
        return a%c
    elif b%2 == 0:
        k = func(a, b//2)
        return k*k%c
    else:
        k = func(a, (b-1)//2)
        return k*k*a%c
a,b,c = map(int, sys.stdin.readline().split())
print(func(a,b))