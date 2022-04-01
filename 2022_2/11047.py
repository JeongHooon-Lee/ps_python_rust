import sys

N, K = map(int, sys.stdin.readline().split())
arr : list = []
answer = 0

for i in range(N):
    arr.append(int(sys.stdin.readline()))

for i in range(N):
    if K == 0:
        break
    if K//arr[N-1-i] > 0:
        answer +=K//arr[N-1-i]
        K = K%arr[N-1-i]

print(answer)