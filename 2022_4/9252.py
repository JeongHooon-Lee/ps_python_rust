import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
a = "0"+a
b = "0"+b

dp = [ [0]*len(a) for _ in range(len(b)) ]
max_of_dp = -1
max_of_dp_index = []
for i in range(1,len(b)):
    for j in range(1,len(a)):
        if a[j] != b[i]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        elif a[j] == b[i]:
            dp[i][j] = dp[i-1][j-1]+1
        if max_of_dp<dp[i][j]:
            max_of_dp=dp[i][j]
            max_of_dp_index=[i,j]

print(max_of_dp)
res = []
while max_of_dp:
    x = max_of_dp_index[0]
    y = max_of_dp_index[1]

    if a[y] == b[x]:
        res.append(a[y])
        max_of_dp_index[0] -=1
        max_of_dp_index[1] -=1
        max_of_dp -=1
    else:
        if dp[x-1][y]>dp[x][y-1]:
            max_of_dp_index[0]-=1
        else:
            max_of_dp_index[1]-=1
res.reverse()
print(str("".join(res)))