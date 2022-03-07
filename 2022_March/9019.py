import sys
from collections import deque

def D(n):
    return (2*n)%10000
def S(n):
    if n == 0:
        return 9999
    else: 
        return n-1
def L(n):
    return (n%1000)*10+n//1000

def R(n):
    return 1000*(n%10)+n//10

for i in range(int(input())):
    A, B = sys.stdin.readline().split()
    queue = deque()
    queue.append((int(A),''))
    visited = [False]*10000

    while queue:
        num, operator = queue.popleft()
        if num == int(B):
            print(operator)
            break
        
        temp = D(num)
        if not visited[temp]:
            queue.append((D(num),operator+"D"))
            visited[temp] = True
        
        temp = S(num)
        if not visited[temp]:
            queue.append((S(num),operator+"S"))
            visited[temp] = True
        
        temp = L(num)
        if not visited[temp]:
            queue.append((L(num),operator+"L"))
            visited[temp] = True

        temp = R(num)
        if not visited[temp]:
            queue.append((R(num),operator+"R"))
            visited[temp] = True