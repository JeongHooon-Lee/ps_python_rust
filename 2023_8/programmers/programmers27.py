# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    count = {i: 0 for i in range(1, N+2)}

    for stage in stages:
        count[stage] += 1

    dp = [count[N+1] + count[N]]
    for i in range(N - 1, 0, -1):
        dp.append(dp[-1] + count[i])
    dp.append(0)
    dp = dp[::-1]
    answer = list(map(lambda x: x[1], sorted([[count[i]/dp[i], i] if dp[i] != 0 else [0, i]
                                              for i in range(1, N + 1)], key=lambda x: x[0], reverse=True)))
    return answer


# [3,4,2,1,5]
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
