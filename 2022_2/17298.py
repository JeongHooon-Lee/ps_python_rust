import sys

N = int(input())
a = list(map(int, sys.stdin.readline().split()))

stack = [0]
answer = [-1] * N

for i in range(1,N):
    while stack and a[i] > a[stack[-1]]:
        answer[stack.pop()] = a[i]
    stack.append(i)

print(*answer)