import sys

R, C = map(int, sys.stdin.readline().split())

matrix : list = []
alpha_visited = [False] * 26
visited = [ [False] * C for _ in range(R) ]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1] 
# A -> 65, Z-> 90

for i in range(R):
    temp = (" ".join(sys.stdin.readline())).split()
    matrix.append(temp)

alpha_visited[ord(matrix[0][0])-65] = True
visited[0][0] = True
res = 0

def dfs(y, x, cnt):
    global res
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C: 
            alpha_index = ord(matrix[ny][nx])-65
            if not visited[ny][nx] and not alpha_visited[alpha_index]:
                visited[ny][nx] = True
                alpha_visited[alpha_index] = True
                dfs(ny, nx, cnt+1)
                visited[ny][nx] = False
                alpha_visited[alpha_index] = False
    res = max(res, cnt)

dfs(0, 0, 1)
print(res)

# pypy