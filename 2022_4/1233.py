import sys

a, b, c = list(map(int, sys.stdin.readline().split()))
res = [0] * (a+b+c+1)

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            res[i+j+k] += 1

print(res.index(max(res)))
