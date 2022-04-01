import sys

N = int(input().strip())
arr = list(map(int, sys.stdin.readline().split()))
print(max(arr)*min(arr))
