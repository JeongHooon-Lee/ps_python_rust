import sys

N, K = map(int, sys.stdin.readline().split())
datas = min(sorted(list(map(int, sys.stdin.readline().split())))[-K:])
print(datas)
