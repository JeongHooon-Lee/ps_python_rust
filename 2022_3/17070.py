import sys
N = int(input())
matrix : list = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
dp = [ [[0]*3 for _ in range(N)] for _ in range(N)]
#dp[i][j][k] matrix[i][j]에 온 종류를 모양에 따라 나눔 k=0 가로 k=1 세로 k=2 대각선
dp[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if matrix[i][j] == 0 and matrix[i-1][j] == 0 and matrix[i][j-1] == 0:
            dp[i][j][2] += sum(dp[i-1][j-1][k] for k in range(3))
        if matrix[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
print(sum(dp[-1][-1][i] for i in range(3)))

# for i in range(N):
#     for j in range(N):
#         print(dp[i][j][0], end=" ")
#     print()
# print()
# for i in range(N):
#     for j in range(N):
#         print(dp[i][j][1], end=" ")
#     print()
# print()
# for i in range(N):
#     for j in range(N):
#         print(dp[i][j][2], end=" ")
#     print()    
# import sys
# from collections import deque

# N = int(input())
# matrix = []
# for i in range(N):
#     matrix.append(list(map(int, sys.stdin.readline().split())))
# dy =[[0,1],[0,1,1],[1,1]]
# dx =[[1,1],[1,1,0],[0,1]]
# def bfs():
#     res = 0
#     queue = deque()
#     queue.append((0,1,0)) #(y,x,state: 0->가로 2->세로 1-> 대각선, count : 이동숫자)

#     while queue:
#         y,x,state= queue.popleft()
#         if y == N-1 and x == N-1:
#             res +=1
#             continue
#         temp = 2 if state == 0 or state == 2 else 3

#         for i in range(temp):
#             ny = y+dy[state][i]
#             nx = x+dx[state][i]
#             if 0<=ny<N and 0<=nx<N and matrix[ny][nx] != 1:
#                 if i == 1 and (matrix[y+1][x]==1 or matrix[y][x+1]==1):
#                     continue
#                 elif i == 0 and state == 2: 
#                     queue.append((ny,nx,2))
#                     continue
#                 else:
#                     queue.append((ny,nx,i))
#     return res
# print(bfs())

####################### time out 