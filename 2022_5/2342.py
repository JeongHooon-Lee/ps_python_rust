import sys

data = list(map(int, sys.stdin.readline().split()))[:-1]
matrix = [[[sys.maxsize]*5 for _ in range(5)] for _ in range(len(data)+1)]
matrix[-1][0][0] = 0


def cost(from_, to_):
    if from_ == 0:
        if to_ == 0:
            return 0
        else:
            return 2
    elif from_ == to_:
        return 1
    elif abs(from_-to_) == 2:
        return 4
    else:
        return 3


# matrix[i][j][k] = i번째 지시사항까지 고려하고, 왼쪽 발과 오른쪽 발이(j, k)에 있을 때 최소의 힘
for i in range(len(data)):
    target = data[i]

    for j in range(5):
        for k in range(5):
            costs = cost(k, target)
            matrix[i][target][j] = min(
                matrix[i][target][j], matrix[i-1][k][j] + costs)

    for j in range(5):
        for k in range(5):
            costs = cost(k, target)
            matrix[i][j][target] = min(
                matrix[i][j][target], matrix[i-1][j][k] + costs)
res = sys.maxsize
for i in range(5):
    for j in range(5):
        res = min(res, matrix[-2][i][j])
print(res)
# 1. 그 발판에 이미 발이 있을때 -> 1
# 2. 중앙에 발이 있을때 -> 2
# 3. 그 양옆 발판에 발이 있을때 -> 3
# 4. 그 반대편에 발이 있을때 -> 4
