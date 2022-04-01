import sys

N = int(sys.stdin.readline())
array = [] 
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,N):
    array[i][0] += array[i-1][0]
    for k in range(1,len(array[i])-1):
        array[i][k] = max(array[i-1][k-1],array[i-1][k])+array[i][k]
    array[i][-1] += array[i-1][-1]

print(max(array[N-1]))