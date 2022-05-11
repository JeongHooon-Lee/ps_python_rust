import sys

A, B = map(int, sys.stdin.readline().split())
res: dict = {}

a_input = list(map(int, sys.stdin.readline().split()))

for i in a_input:
    res[i] = 1

b_input = list(map(int, sys.stdin.readline().split()))

for i in b_input:
    try:
        if res[i]:
            del res[i]
    except:
        res[i] = 1

print(len(res))
