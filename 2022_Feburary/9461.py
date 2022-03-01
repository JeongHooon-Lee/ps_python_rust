import sys
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

def func(N):
    if dp[N]:
        return(dp[N])
    dp[N] = func(N-2)+func(N-3)
    return(dp[N])

for i in range(int(input())):
    N = int(sys.stdin.readline().strip())

    print(func(N))