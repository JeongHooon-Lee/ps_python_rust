import sys

N, B = map(int, sys.stdin.readline().split())
arr : list = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

def multiplay_matrix(array1,array2):
    array3 = [ [0] * N for _ in range(N) ] 
    for i in range(N):
        for j in range(N):
            for k in range(N):
                array3[i][j] += array1[i][k]%1000 * array2[k][j]%1000
            array3[i][j] %= 1000
    return array3

def doubled_matrix(array1):
    array3 = [ [0] * N for _ in range(N) ] 
    for i in range(N):
        for j in range(N):
            for k in range(N):
                array3[i][j] += array1[i][k]%1000 * array1[k][j]%1000
            array3[i][j] %= 1000
    return array3

def func(array,b):
    if b == 1:
        res_array = array
        for i in range(N):
            for j in range(N):
                res_array[i][j] = array[i][j]%1000
        return res_array
    if b == 2:
        return multiplay_matrix(array,array)
    elif b%2 == 0:
        return doubled_matrix(func(array,b//2)) 
    else:
        return multiplay_matrix(array,doubled_matrix(func(array,b//2)))

for i in func(arr,B):
    print(*i)

