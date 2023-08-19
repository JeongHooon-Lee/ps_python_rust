import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dict = {i: 0 for i in range(1, 1000001)}
for i in arr:
    dict[i] += 1

stack = [0]
result = [-1] * N

for i in range(1, N):
    v = arr[i]
    while stack and dict[arr[stack[-1]]] < dict[v]:
        result[stack.pop()] = v
    stack.append(i)
print(*result)
