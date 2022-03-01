import sys

N = int(sys.stdin.readline())
visited = [ False for _ in range(N*N)]
graph = [ [] for _ in range(N*N)]
array = []
answer = []
count = 0
def R_graph(inx):
    if array[inx] == "1" and array[inx+1] == "1":
        if inx+1 not in graph[inx]:
            graph[inx].append(inx+1)
        if inx not in graph[inx+1]:
            graph[inx+1].append(inx)
def L_graph(inx):
    if array[inx] == "1" and array[inx-1] == "1":
        if inx-1 not in graph[inx]:
            graph[inx].append(inx-1)
        if inx not in graph[inx-1]:
            graph[inx-1].append(inx)
def U_graph(inx):
    if array[inx] == "1" and array[inx-N] == "1":
        if inx-N not in graph[inx]:
            graph[inx].append(inx-N)
        if inx not in graph[inx-N]:
            graph[inx-N].append(inx)
def D_graph(inx):
    if array[inx] == "1" and array[inx+N] == "1":
        if inx+N not in graph[inx]:
            graph[inx].append(inx+N)
        if inx not in graph[inx+N]:
            graph[inx+N].append(inx)

def dfs(inx):
    result = 1
    visited[inx] = True
    for i in graph[inx]:
        if visited[i] == False:
            visited[i] = True
            result+=dfs(i)
    return result
for i in range(N):
    temp = list(sys.stdin.readline().strip())
    array += list("".join(temp))
#print(array)

for i in range(N*N):
    if array[i] == "1":
        if i%N != N-1:
            R_graph(i)
        if i%N != 0:
            L_graph(i)
        if i>=N:
            U_graph(i)
        if i<N*(N-1):
            D_graph(i)

for i in range(N*N):
    if visited[i] == False and array[i] == "1":
        answer.append(dfs(i))
        count+=1

print(count)

for i in sorted(answer):
    print(i)