import sys

N = int(input())
data: list = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    data.append(A-B)
data.sort()

if N % 2 == 1:
    print(1)
else:
    print(abs(data[N//2] - data[N//2-1])+1)
