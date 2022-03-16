import sys
from math import gcd
moduler = 1000000007

def fast_zegop(N,exp): 
    if exp == 1:
        return N
    if exp % 2 == 0:
        half = fast_zegop(N, exp//2)
        return  half * half % moduler
    else:
        return N * fast_zegop(N,exp-1) % moduler
sum = 0
for i in  range(int(input())):
    N, S = map(int, sys.stdin.readline().split())
    gcdnum = gcd(N,S)
    N = N // gcdnum
    S = S // gcdnum

    sum += S * fast_zegop(N, moduler-2) % moduler
    sum %= moduler
print(sum)