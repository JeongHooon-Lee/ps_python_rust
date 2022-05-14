# pypy
import sys

S = sys.stdin.readline().strip()
N = int(input())

dp = [[0]*(len(S)+1) for _ in range(26)]

for i in range(26):
    for j in range(1, len(S)+1):
        dp[i][j] = dp[i][j-1]
        dp[ord(S[j-1])-97][j] = dp[ord(S[j-1])-97][j-1] + 1


for i in range(N):
    target, start, to = sys.stdin.readline().split()
    start = int(start)+1
    to = int(to)+1
    sys.stdout.write(str(dp[ord(target)-97][to]-dp[ord(target)-97][start-1]))
