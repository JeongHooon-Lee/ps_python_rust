#https://www.acmicpc.net/problem/2630
import sys

def check(arr,length):
    temp = arr[0][0]
    for i in range(length):
        for j in range(length):
            if temp != arr[i][j]:
                return -1
    if temp == 1:
        return 1
    elif temp == 0:
        return 0
        
def div(arr,N):
    temp = check(arr,N)
    if  temp == 1:
        return [0,1]
    elif temp == 0:
        return [1,0] 
    answer : list = [0, 0] 
    array : list = [ [] for _ in range(4) ]
    for i in range(N//2):
        array[0].append(arr[i][:N//2])
        array[1].append(arr[i][N//2:])
        array[2].append(arr[N//2+i][:N//2])
        array[3].append(arr[N//2+i][N//2:])
    
    for i in range(4):
        if check(array[i],N//2)==1:
            answer[1] += 1
        elif check(array[i],N//2) == 0:
            answer[0] += 1
        else:
            result = div(array[i],N//2)
            answer[0]+=result[0]
            answer[1]+=result[1]
    return answer
    
input_array : list = []
n = int(sys.stdin.readline().strip())
for i in range(n):
    input_array.append(list(map(int, sys.stdin.readline().split())))
for i in div(input_array,n):
    print(i)