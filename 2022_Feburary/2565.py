import sys

N = int(input().strip())
a : list = []
dp = [0]*N
answer = -1
for i in range(N):
    a.append(list(map(int, sys.stdin.readline().split())))

a.sort(key=lambda x:x[0])


for i in range(N):
    for j in range(i):
        if a[i][1] > a[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i]+=1
    if answer < dp[i]:
        answer = dp[i]
print(N-answer)