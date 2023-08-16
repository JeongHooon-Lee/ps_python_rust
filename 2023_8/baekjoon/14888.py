import sys
import copy
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
# [+, -, x, /]
op = list(map(int, sys.stdin.readline().split()))

result = [-1e9, 1e9]


def recursion(ops: list, remain_op):
    if len(ops) == N - 1:
        res = A[0]
        for i in range(1, N):
            if ops[i - 1] == 0:
                res = res + A[i]
            elif ops[i - 1] == 1:
                res = res - A[i]
            elif ops[i - 1] == 2:
                res = res * A[i]
            else:
                if res < 0:
                    res = -(abs(res) // A[i])
                else:
                    res = res // A[i]
        result[0] = max(result[0], res)
        result[1] = min(result[1], res)
        return
    for i in range(4):
        if remain_op[i] > 0:
            new_remain_op = copy.deepcopy(remain_op)
            new_remain_op[i] -= 1
            recursion(ops + [i], new_remain_op)


ops = []
recursion(ops, op)
for re in result:
    print(int(re))
