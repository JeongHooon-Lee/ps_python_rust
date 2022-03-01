#https://www.acmicpc.net/problem/2579
import sys

#def func(inx):
    
array : list = []
answer : list = []
n=int(input())
for i in range(n):
    array.append(int(input()))


if n ==1:
    print(array[0])
    quit()

answer.append(sum(array[:1])) # 0
answer.append(sum(array[:2])) # 1

if n >= 3:
    # 3
    answer.append(array[2] + max(array[0],array[1]))
    
    # bigger than 3
    for i in range(3,n):
        answer.append(max(array[i]+array[i-1]+answer[i-3], array[i]+answer[i-2]))

print(answer[n-1])