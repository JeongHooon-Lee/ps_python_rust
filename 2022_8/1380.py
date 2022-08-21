import sys

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if not n:
        exit()
    dict = {}
    names = {}
    for i in range(n):
        names[i] = list(map(str, sys.stdin.readline().split()))
        dict[i] = 0
    for i in range(2*n-1):
        data = list(map(str, sys.stdin.readline().split()))
        dict[int(data[0])-1] += 1
    for i in dict.keys():
        if dict[i] != 2:
            print(cnt, *names[i])
            break
