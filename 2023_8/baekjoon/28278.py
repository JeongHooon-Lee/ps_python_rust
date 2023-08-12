import sys
N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    order = list(map(int, sys.stdin.readline().split()))
    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        print("-1" if not stack else stack.pop())
    elif order[0] == 3:
        print(len(stack))
    elif order[0] == 4:
        print(1 if not stack else 0)
    elif order[0] == 5:
        print(-1 if not stack else stack[-1])
