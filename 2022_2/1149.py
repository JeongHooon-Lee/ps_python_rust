import sys

N = int(sys.stdin.readline().strip())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

for i in range(1,N):
    array[i][0] = min(array[i-1][1],array[i-1][2])+array[i][0]
    array[i][1] = min(array[i-1][0],array[i-1][2])+array[i][1]
    array[i][2] = min(array[i-1][0],array[i-1][1])+array[i][2]
print(min(array[N-1][0],array[N-1][1],array[N-1][2]))

