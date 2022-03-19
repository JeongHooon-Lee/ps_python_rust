import sys

N = int(sys.stdin.readline().strip())
matrix : list = []
max_dp = [ [0]*3 for _ in range(2)]
min_dp = [ [0]*3 for _ in range(2)]
temp = 1
for i in range(N):
    matrix = list(map(int, sys.stdin.readline().split()))
    if i==0:
        for j in range(3):
            max_dp[0][j] = matrix[j]
            min_dp[0][j] = matrix[j]
    else:
        k = 1 if temp == 1 else 0
        l = 0 if temp == 1 else 1
        max_dp[k][0] = max(max_dp[l][0], max_dp[l][1]) + matrix[0]
        max_dp[k][1] = max(max_dp[l][0], max_dp[l][1], max_dp[l][2]) + matrix[1]
        max_dp[k][2] = max(max_dp[l][1], max_dp[l][2]) + matrix[2]

        min_dp[k][0] = min(min_dp[l][0], min_dp[l][1]) + matrix[0]
        min_dp[k][1] = min(min_dp[l][0], min_dp[l][1], min_dp[l][2]) + matrix[1]
        min_dp[k][2] = min(min_dp[l][1], min_dp[l][2]) + matrix[2]
        temp *= -1

# for i in range(2):
#     print(max_dp[i])
#     print(min_dp[i])
if N%2 == 0:
    print(max(max_dp[1]), min(min_dp[1]))
else:
    print(max(max_dp[0]), min(min_dp[0]))
    