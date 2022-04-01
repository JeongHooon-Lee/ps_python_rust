import sys
from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]
def dfs(current):
    queue = deque()
    queue.append(current)
    visited_count[current[0]][current[1]] = 1
    
    while queue:
        a, b = queue.popleft()
        if [a, b] == To:
            print(visited_count[a][b]-1)
            return

        for i in range(8):
            temp_ : list = [a, b]
            temp_[0] += dy[i]
            temp_[1] += dx[i]
            if 0 <= temp_[0] < I and 0 <= temp_[1] <I and not visited_count[temp_[0]][temp_[1]]:
                queue.append(temp_)
                visited_count[temp_[0]][temp_[1]] = visited_count[a][b]+1

for i in range(int(input())):
    I = int(sys.stdin.readline())
    visited_count = [ [0]*I for _ in range(I) ]
    From = list(map(int, sys.stdin.readline().split()))
    To = list(map(int, sys.stdin.readline().split()))
    dfs(From)
