import sys

sys.setrecursionlimit(10**6)

N = int(input())
W = int(input())
dp = [[-1 for _ in range(W+2)] for _ in range(W+2)]
cases = [[1, 1], [N, N]]
for i in range(W):
    cases.append(list(map(int, sys.stdin.readline().split())))


def solution(first_caps, second_caps):
    if first_caps > W or second_caps > W:
        return 0
    if dp[first_caps][second_caps] != -1:
        return dp[first_caps][second_caps]

    next_case = max(first_caps, second_caps) + 1

    next_x = solution(next_case, second_caps) + abs(
        cases[next_case][0] - cases[first_caps][0]) + abs(cases[next_case][1] - cases[first_caps][1])
    next_y = solution(first_caps, next_case) + abs(
        cases[next_case][0] - cases[second_caps][0]) + abs(cases[next_case][1] - cases[second_caps][1])
    dp[first_caps][second_caps] = min(next_x, next_y)
    return dp[first_caps][second_caps]


def result(first_caps, second_caps):
    if first_caps > W or second_caps > W:
        return
    next_case = max(first_caps, second_caps) + 1
    next_x = abs(cases[next_case][0] - cases[first_caps][0]) + \
        abs(cases[next_case][1] - cases[first_caps][1])
    next_y = abs(cases[next_case][0] - cases[second_caps][0]) + \
        abs(cases[next_case][1] - cases[second_caps][1])

    if dp[next_case][second_caps] + next_x < dp[first_caps][next_case] + next_y:
        print(1)
        result(next_case, second_caps)
    else:
        print(2)
        result(first_caps, next_case)
    return


print(solution(0, 1))
result(0, 1)
