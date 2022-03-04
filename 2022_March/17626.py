import sys
from math import sqrt

N = int(input())
dp = [0, 1]

for i in range(2, N+1):
    temp = int(sqrt(i))
    min_value = 1e9
    for j in range(1,temp+1):
        min_value = min(min_value, dp[i-(j**2)])
    dp.append(min_value+1)

print(dp[N])