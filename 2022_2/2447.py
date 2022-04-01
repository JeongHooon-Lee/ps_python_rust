import sys

def solution(n):
    global array
    if n==3:
        array[0][:3] = array[2][:3] = [1] * 3
        array[1][:3] = [1,0,1]
        return

    a = n//3
    solution(a)

    for i in range(3):
        for j in range(3):
            if i==1 and j == 1:
                continue
            else:
                for k in range(a):
                    array[a*i+k][a*j:a*(j+1)] = array[k][:a]
N = int(sys.stdin.readline().strip())
array = [ [0 for _ in range(N)] for _ in range(N) ]
solution(N)

for i in array:
    for j in i:
        if j == 1:
            print("*",end='')
        else:
            print(" ",end='')
    print()