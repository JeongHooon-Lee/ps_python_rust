import sys

N = int(input())
values = list(map(int, sys.stdin.readline().split()))
min_values: list = []
if N == 1:
    print(sum(values) - min(values))
else:
    min_values.append(min(values[0], values[-1]))
    min_values.append(min(values[1], values[4]))
    min_values.append(min(values[2], values[3]))
    min_values.sort()

    shape_1 = 4*(N-1)*(N-2) + (N-2)**2
    shape_2 = 4*(2*N-3)
    shape_3 = 4
    res = shape_1*min_values[0] + shape_2 * \
        sum(min_values[:2]) + shape_3*sum(min_values)
    print(res)

# # 한면만 나오는 수
# 4 * (N-1) * (N-2) + (N-2)**2

# # 두 면만 나오는 수
# 4*(N-1) + 4*(N-2)

# # 세 면만 나오는 수
# 4
