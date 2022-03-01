import sys

N = int(input().strip())
A = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

maximum = -1e9
minimum = 1e9

def dfs(depth, value, plus, minus, multiplay, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(maximum, value)
        minimum = min(minimum, value)
        return
    
    if plus:
        dfs(depth+1, value + A[depth], plus-1, minus, multiplay, divide)
    if minus:
        dfs(depth+1, value - A[depth], plus, minus-1, multiplay, divide)
    if multiplay:
        dfs(depth+1, value * A[depth], plus, minus, multiplay-1, divide)
    if divide:
        dfs(depth+1, int(value / A[depth]), plus, minus, multiplay, divide-1)

dfs(1,A[0],operator[0],operator[1],operator[2],operator[3])
print(maximum)
print(minimum)