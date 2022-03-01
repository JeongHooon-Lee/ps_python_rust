import sys

def solution(n):
    if len(array)-1 == n:
            return array[n]
    else:
        array.append(array[-1]+array[-2])
        return solution(n)

array = [0,1]
n = int(sys.stdin.readline().strip())
if n < 2:
    print(array[n])
else:
    print(solution(n))
    

