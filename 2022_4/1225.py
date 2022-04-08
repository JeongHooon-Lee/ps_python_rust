import sys

A, B = sys.stdin.readline().split()
print(sum(list(map(int, A))) * sum(list(map(int, B))))