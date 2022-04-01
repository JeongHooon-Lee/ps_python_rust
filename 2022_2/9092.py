import sys
from math import sqrt
def solution(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return 0
    return n
sosu : list = []

for i in range(2,10000):
    temp = solution(i)
    if temp != 0:
        sosu.append(temp)

for i in range(int(sys.stdin.readline().strip())):
    a = int(sys.stdin.readline().strip())
    b = a // 2
    for j in range(b, 1, -1):
        if a-j in sosu and j in sosu:
            print(j, a - j)
            break
    