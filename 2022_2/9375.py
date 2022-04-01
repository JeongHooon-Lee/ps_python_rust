import sys

for i in range(int(input())):
    arr : dict = {}
    answer = 1
    for j in range(int(input())):
        a, b = sys.stdin.readline().strip().split()
        if b not in arr.keys():
            arr[b] = 1
        else:
            arr[b] += 1
        
    for k in arr.values():
        answer *= (k+1)
        
    print(answer-1)