import sys

N, L = map(int, sys.stdin.readline().split())
x = -1

for i in range(L, 101):
    temp = N-(i*i-i)/2
    if temp % i == 0 and temp // i >= 0:
        c = temp // i
        x = 0

        for j in range(i):
            print(int(c+j), end=" ")
        break

if x == -1:
    print(x)
