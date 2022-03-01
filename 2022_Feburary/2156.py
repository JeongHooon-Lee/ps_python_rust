import sys

N = int(input().strip())
array = []
dp = [0]*N
for i in range(N):
    array.append(int(sys.stdin.readline().strip()))
dp[0] = array[0]
if N==1:
    print(dp[0])
    quit()
dp[1] = array[0]+array[1]
if N==2:
    print(dp[1])
    quit()
dp[2] = max(dp[1],array[1]+array[2],array[0]+array[2])
if N==3:
    print(dp[2])
    quit()

for i in range(3,N):
    dp[i] = max(dp[i-1],dp[i-3]+array[i-1]+array[i],dp[i-2]+array[i])
print(dp[N-1])