# pypy
import sys

A, B = map(int, sys.stdin.readline().split())
datas = [0] * (B+1)
primes: dict = {}
res = 0
for i in range(2, B+1):
    if not datas[i]:
        primes[i] = 1
    for j in range(i*2, B+1, i):
        datas[j] = 1

for i in range(A, B+1):
    temp = i
    cnt = 0
    while True:
        for j in primes.keys():
            if temp % j == 0:
                temp //= j
                cnt += 1
        if temp == i or temp == 1:
            break
    try:
        if primes[cnt]:
            res += 1
    except:
        continue
print(res)
