import sys

str = sys.stdin.readline().strip()
res: dict = {}

for i in range(1, len(str)+1):
    for j in range(0, len(str)-i+1):
        res[str[j:j+i]] = 1

print(len(res))
