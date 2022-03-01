import sys
from math import sqrt

def condition(x,Num):
    return x>Num and x<=Num*2

def solution(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return 0
    return 
    

sosu = []
for i in range(2,123456*2+1):
    if solution(i) != 0:
        sosu.append(i)

while True:
    num = int(sys.stdin.readline().strip())
    if num == 0:
        break

    print(sum(1 for x in sosu if condition(x,num)))

