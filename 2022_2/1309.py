import sys

N= int(input())
dp = [0]*N
dp[0] = 3
if N < 2:
    print(dp[0])
    quit()
else:
    dp[1] = 7
    for i in range(2,N):
        dp[i] = (((dp[i-1]*2)%9901) + dp[i-2]%9901)%9901
print(dp[N-1])