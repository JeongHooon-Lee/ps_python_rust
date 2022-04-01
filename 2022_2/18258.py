import sys

arr : list = []
for i in range(int(input())):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        arr.append(int(a[1]))
    elif a[0] == "pop":
        if arr:
            print(arr[0])
            arr = arr[1:]
        else:
            print(-1)
    elif a[0] == "size":
        print(len(arr))
    elif a[0] == "empty":
        if arr:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif a[0] == "back":
        if arr:
            print(arr[-1])
        else:
            print(-1)