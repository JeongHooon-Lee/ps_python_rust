import sys

s = sys.stdin.readline().strip()
banned = sys.stdin.readline().strip()
stack = []

for i in s:
    stack.append(i)
    if i == banned[-1] and stack[-len(banned):] == list(banned):
        for i in range(len(banned)):
            stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")