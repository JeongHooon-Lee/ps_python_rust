import sys
from math import sqrt

def solution(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return i
    return -1

N = int(sys.stdin.readline().strip())
if N==1:
    quit()
answer : list = [] 
answer.append(N)

while True:
    temp = solution(answer[-1])
    if temp == -1:
        break
    else:
        answer.append(temp)
        answer.append(answer.pop(-2)//temp)

for i in answer:
    print(i)
