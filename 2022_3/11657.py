import sys
INF = int(1e9)
N, M = map(int, sys.stdin.readline().split())
edge : list = []
dp : list = [INF]*(N+1)
for i in range(M):
    edge.append(list(map(int, sys.stdin.readline().split())))
dp[1] = 0
answer = -1
for k in range(N):
    for i in edge:
        if dp[i[0]] == INF:
            continue
        elif dp[i[0]] + i[2] < dp[i[1]]:
            dp[i[1]] = dp[i[0]] + i[2]
            if k == N-1:
                answer =1

if answer == 1:
    print(-1)
else:
    for i in dp[2:]:
        print(-1 if i == INF else i)