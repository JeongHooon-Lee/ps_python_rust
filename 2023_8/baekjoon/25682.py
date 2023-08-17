import sys

N, M, K = map(int, sys.stdin.readline().split())
arr = [list(str(sys.stdin.readline().strip())) for _ in range(N)]


def solution(color):
    pre_sum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 0:
                if arr[i][j] != color:
                    value = 1
                else:
                    value = 0
            else:
                if arr[i][j] == color:
                    value = 1
                else:
                    value = 0
            pre_sum[i + 1][j + 1] = pre_sum[i][j + 1] + \
                pre_sum[i + 1][j] - pre_sum[i][j] + value
    result = N * M
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            result = min(result, pre_sum[i + K - 1][j + K - 1] - pre_sum[i - 1]
                         [j + K - 1] - pre_sum[i + K - 1][j - 1] + pre_sum[i - 1][j - 1])
    return result


print(min(solution('B'), solution('W')))
