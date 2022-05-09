import sys

N, M = map(int, sys.stdin.readline().split())
S: dict = {}
for i in range(N):
    S[sys.stdin.readline().strip()] = True
res = 0

for i in range(M):
    temp = sys.stdin.readline().strip()
    if temp in S.keys():
        res += 1

print(res)
# codeplus

# startlink

# sundaycoding
# codingsh
