import sys

N = int(input().strip())
arr = [[1, 1],[1, 0]]

q = 1000000007
def multiplay_matrix(array1,array2):
    array3 = [ [0] * 2 for _ in range(2) ] 
    for i in range(2):
        for j in range(2):
            for k in range(2):
                array3[i][j] += array1[i][k]%q * array2[k][j]%q
            array3[i][j] %= q
    return array3

def doubled_matrix(array1):
    array3 = [ [0] * 2 for _ in range(2) ] 
    for i in range(2):
        for j in range(2):
            for k in range(2):
                array3[i][j] += array1[i][k]%q * array1[k][j]%q
            array3[i][j] %= q
    return array3

def func(array,b):
    if b == 1:
        res_array = array
        for i in range(2):
            for j in range(2):
                res_array[i][j] = array[i][j]%q
        return res_array
    if b == 2:
        return multiplay_matrix(array,array)
    elif b%2 == 0:
        return doubled_matrix(func(array,b//2)) 
    else:
        return multiplay_matrix(array,doubled_matrix(func(array,b//2)))
        
print(func(arr,N)[1][0]) 