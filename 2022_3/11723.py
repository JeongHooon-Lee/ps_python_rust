import sys

s : list = [0]*21
for i in range(int(input())):
    a = sys.stdin.readline().strip().split()
    
    if a[0] == "add" and not s[int(a[1])]:
        s[int(a[1])] = 1
    elif a[0] == "remove" and s[int(a[1])]:
        s[int(a[1])] = 0
    elif a[0] == "check":
        print(s[int(a[1])])
    elif a[0] == "toggle":
        if s[int(a[1])]:
            s[int(a[1])] = 0
        else:
            s[int(a[1])] = 1
    elif a[0] == "all":
        s = [ 1 for i in range(21) ]
    elif a[0] == "empty":
        s = [0]*21