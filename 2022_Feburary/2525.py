import sys

H, M = map(int, sys.stdin.readline().split())
t = int(input().strip())
tempH = t//60
tempM = t%60
H += tempH
M += tempM

if M >= 60:
    H += M//60
    M %= 60

H = H%24
print(H, M)
