import sys

A, B = sys.stdin.readline().strip().split()
res = 50

for i in range(len(B)-len(A)+1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[j+i]:
            cnt += 1
    res = min(cnt, res)
print(res)
