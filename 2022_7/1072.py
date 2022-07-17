import sys

X, Y = map(int, sys.stdin.readline().split())


def score(x, y):
    return y * 100 // x


current = score(X, Y)

if score(X, Y) >= 99:
    print(-1)
    exit()
left = 1
right = X
while left <= right:
    mid = (left + right)//2
    temp_1 = score(X+mid, Y+mid)
    temp_2 = score(X+mid-1, Y+mid-1)
    if current != temp_1 and current == temp_2:
        print(mid)
        break
    elif current == temp_1 and current == temp_2:
        left = mid + 1
    elif current != temp_1 and current != temp_2:
        right = mid - 1
