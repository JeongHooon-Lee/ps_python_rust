import sys

N = int(sys.stdin.readline())
distance  = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
answer = 0
m = oil[0]

for i in range(N-1):
    if m > oil[i]:
        m = oil[i]
    answer += m * distance[i]
print(answer)