import sys
import math
for _ in range(int(input())):
    N, M, W = map(int, sys.stdin.readline().split())
    edge : list = []
    for i in range(M):
        s, e, t = map(int, sys.stdin.readline().split())
        edge.append([s,e,t])
        edge.append([e,s,t])
    for i in range(W):
        s, e, t = map(int, sys.stdin.readline().split())
        edge.append([s,e,-t])

    dp = [100001] * (N+1)
    dp[1] = 0
    answer = -1
    for i in range(N):
        for j in edge:
            if dp[j[0]] + j[2] < dp[j[1]]:
                dp[j[1]] = dp[j[0]] + j[2]
                if i == N-1:
                    answer = 1
             

    if answer == 1:
        print("YES")
    else:
        print("NO")