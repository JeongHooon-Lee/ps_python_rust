import math
import sys

A, B = map(int, sys.stdin.readline().split())


def solution(x):
    if x <= 0:
        return 0

    temp = int(math.log2(x))
    pow2 = 2**temp
    if pow2 == x:
        return temp * x // 2 + 1

    diff = x - pow2
    return solution(pow2) + diff + solution(diff)


print(solution(B) - solution(A-1))
