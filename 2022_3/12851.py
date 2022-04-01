import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

visited = [ [-1, 0] for _ in range(100001)]
def func():
    visited[N][0] = 0
    visited[N][1] = 1
    queue =deque()
    queue.append(N)

    while queue:
        num = queue.popleft()
        
        for i in [num-1, num+1, num*2]:
            if 0<= i<= 100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[num][0]+1
                    visited[i][1] = visited[num][1]
                    queue.append(i)
                elif visited[i][0] == visited[num][0]+1:
                    visited[i][1] += visited[num][1]
func()
print(visited[K][0])
print(visited[K][1])