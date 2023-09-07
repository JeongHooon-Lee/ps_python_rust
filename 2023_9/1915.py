import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int, "".join(sys.stdin.readline().strip()))))

result = 0
for i in range(N):
    for j in range(M):
        if i >= 1 and j >= 1:
            if arr[i][j] == 1 and arr[i-1][j] != 0 and arr[i][j-1] != 0 and arr[i-1][j-1] != 0:
                arr[i][j] = min(arr[i-1][j], arr[i-1][j-1], arr[i][j-1]) + 1
        result = max(arr[i][j] * arr[i][j], result)
print(result)
