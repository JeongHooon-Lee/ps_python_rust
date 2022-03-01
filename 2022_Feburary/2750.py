import sys

array : list = []
for i in range(int(input())):
    t = int(input().strip())
    array.append(t)

array.sort()

for i in array:
    print(i)