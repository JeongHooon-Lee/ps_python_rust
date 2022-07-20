import sys

L, R = sys.stdin.readline().strip().split()

if len(L) != len(R):
    print(0)
else:
    cnt = 0
    for i in range(len(L)):
        if L[i] != R[i]:
            break
        elif L[i] == R[i] and L[i] == '8':
            cnt += 1
    print(cnt)
