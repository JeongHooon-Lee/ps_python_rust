import sys
a = input()
b = input()
a = "0"+a
b = "0"+b

dp = [ [0]*len(a) for _ in range(len(b)) ]
    
for i in range(1,len(b)):
    for j in range(1,len(a)):
        if a[j] != b[i]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        elif a[j] == b[i]:
            dp[i][j] = dp[i-1][j-1]+1

print(dp[i][j])

        