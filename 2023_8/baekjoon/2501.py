import sys

N, K = map(int, sys.stdin.readline().split())
divisor = [1, N]

for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        divisor.append(i)
        divisor.append(N//i)

divisor = sorted(list(set(divisor)))

print(0 if len(divisor) < K else divisor[K - 1])
