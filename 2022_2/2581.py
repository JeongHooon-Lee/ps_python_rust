import sys
from math import sqrt

def solution(m):
    for i in range(2,int(sqrt(m))+1):
        if m%i == 0:
            return 0
    return 1

M = int(sys.stdin.readline().strip())
if M == 1:
    M = 2
N = int(sys.stdin.readline().strip())
answer : list = [] 
for i in range(M,N+1):
    temp = solution(i)
    
    if temp == 1:  #소수일때
        answer.append(i)

if not answer:
    print("-1")
else:
    print(sum(answer))
    print(min(answer))
