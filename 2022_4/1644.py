import sys

N = int(input())

num_ = [False, False] + [True]*(N-1)
primes = []

for i in range(2, N+1):
    if num_[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            num_[j] = False

left = 0
right = 0
res = 0
while right <= len(primes):
    temp = sum(primes[left:right])
    if N == temp:
        res += 1
        right += 1
    elif N < temp:
        left += 1
    else:
        right += 1
print(res)
