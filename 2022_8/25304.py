import sys

N = int(input())

for i in range(int(input())):
    A, B = map(int, sys.stdin.readline().split())
    N -= A*B

if not N:
    print("Yes")
else:
    print("No")
