import sys

def solution(n):
    if n <= 1:
        return 1
    else:
        return n*solution(n-1)

num = int(sys.stdin.readline().strip())

print(solution(num))