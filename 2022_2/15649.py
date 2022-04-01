import sys
def printit(arr):
    for i in arr:
        print(i,end=" ")
    print()

def DFS(cnt):
    if cnt == M:
        printit(print_array)
        return
        
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            print_array.append(array[i])
            DFS(cnt+1)
            print_array.pop()
            visited[i] = False


N, M = map(int, sys.stdin.readline().split())
visited = [ False for _ in range(N) ]
array = [ i for i in range(1,N+1) ]
print_array = []
DFS(0)