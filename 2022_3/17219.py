import sys

N, M = map(int, sys.stdin.readline().split())
password : dict = {}
for i in range(N):
    a, b = sys.stdin.readline().strip().split()
    password[a] = b

for i in range(M):
    print(password[sys.stdin.readline().strip()])
    