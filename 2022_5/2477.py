import sys

K = int(input())
vertical = []
horizontal = []
all = []

for i in range(6):
    direction, length = map(int, sys.stdin.readline().split())
    all.append(length)
    if direction == 1 or direction == 2:
        horizontal.append(length)
    else:
        vertical.append(length)


def find(arr):
    return all.index(max(arr))


temp1 = abs(all[(find(vertical)-1) % 6] - all[(find(vertical)+1) % 6])
temp2 = abs(all[(find(horizontal)-1) % 6] - all[(find(horizontal)+1) % 6])

print((max(vertical)*max(horizontal) - temp1*temp2) * K)
