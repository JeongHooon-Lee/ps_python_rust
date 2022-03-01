import sys

N, C = map(int, sys.stdin.readline().split())
arr : list = []
for i in range(N):
    arr.append(int(input()))
arr.sort()

def binary():
    left = 1
    right = max(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        count = 1
        wifi = min(arr) + mid

        for i in range(1, len(arr)):
            if wifi <= arr[i]:
                count +=1
                wifi = arr[i] + mid

        if count >= C:
            left = mid + 1
        elif count < C:
            right = mid - 1

    return right
print(binary())
