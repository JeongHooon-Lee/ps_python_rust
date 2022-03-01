import sys
def fast_pow(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        temp = fast_pow(a,b//2)
        return temp*temp%c
    else:
        temp = fast_pow(a,(b-1)//2)
        return temp*temp*a%c

c = 1000000007
N, K = map(int, sys.stdin.readline().split())

dp = [0]*(N+1)
dp[0] = dp[1] = 1
for i in range(2,N+1):
    dp[i] = dp[i-1]*i % c
A = dp[N]
B = (dp[K]*dp[N-K])%c
print( (A%c) * (fast_pow(B,c-2)%c)%c)

