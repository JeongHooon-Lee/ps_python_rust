import sys

N, A, B = map(int, sys.stdin.readline().split())
res = 0

while A != B:
    A -= A//2
    B -= B//2
    res += 1
print(res)
