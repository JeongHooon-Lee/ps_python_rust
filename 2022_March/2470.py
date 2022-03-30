import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
left = 0
right = N-1
diff = arr[-1] - arr[0]
answer = sys.maxsize

while left < right:
    temp = arr[right] + arr[left]
    if abs(temp) < answer:
        answer= abs(temp)
        res = [arr[left], arr[right]]
    if temp < 0:
        left += 1
    else:
        right -=1
print(*res)