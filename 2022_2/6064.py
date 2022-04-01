import sys
from math import gcd

def lcm(a,b):
    return (a*b)//gcd(a,b)


for i in range(int(input())):
    M,N,x,y = map(int,sys.stdin.readline().split())
    answer = x
    y %=N
    while True:
        if answer%N == y:
            print(answer)
            break
        answer+=M
        if answer > lcm(N,M):
            print("-1")
            break
    