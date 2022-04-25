import sys
import math
min_, max_ = map(int, sys.stdin.readline().split())
matrix = [1 for _ in range(min_, max_+1)]
square = [i**2 for i in range(2, int(math.sqrt(max_))+1)]

for i in square:
    idx = (math.ceil(min_/i)*i) - min_
    while idx <= max_ - min_:
        matrix[idx] = 0
        idx += i

print(sum(matrix))
