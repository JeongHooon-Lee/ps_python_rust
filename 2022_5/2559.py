import sys

N, K = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))
left = 0
right = K - 1

temp = sum(data[:right+1])
res = [temp]

while right < N-1:
    right += 1
    temp = temp - data[left] + data[right]
    left += 1

    res = max(res, temp)
print(res)
