import sys

arr = [ [0 for _ in range(100)] for _ in range(100) ]
n = int(sys.stdin.readline().strip())
count : int = 0
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            if arr[j][k] == 0:
                count+=1
                arr[j][k] = 1
print(count)
