import sys
N, K = map(int, sys.stdin.readline().split())
q = 1000000000
dp = [ [0]*(K+1) for _ in range(N+1) ] 
dp[1] = [0] + [ i for i in range(1,K+1) ]
for i in range(2, N+1):
    for j in range(1, K+1):
        dp[i][j] = (dp[i][j-1]%q+dp[i-1][j]%q)%q

print(dp[N][-1])
# (1,1) = 1
# (1,2) = 2
# (1,3) = 3
# (1,4) = 4...

# (2,1) = 1
# (2,2) = 3
# (2,3) = 6
# (2,4) = 10

# 0 20
# 1 19
# 2 18

# 19 1
# 20 0