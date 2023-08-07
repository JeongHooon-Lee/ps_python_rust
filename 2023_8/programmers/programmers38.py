# https://school.programmers.co.kr/learn/courses/30/lessons/86053

def solution(a, b, g, s, w, t):
    answer = 4 * 10 ** 14
    start = 0
    end = 4 * 10 ** 14
    length = len(g)
    while start <= end:
        mid = (end + start) // 2
        values = [0, 0, 0]  # gold, silver, total

        for i in range(length):
            current_values = [g[i], s[i], g[i] + s[i]]
            weight = w[i]
            time = t[i]

            mv_count = (mid - time) // (time * 2) + 1 if mid >= time * 3 else 1
            for j in range(3):
                values[j] += min(current_values[j], mv_count * weight)

        if values[0] >= a and values[1] >= b and values[2] >= a + b:
            end = mid - 1
            answer = min(mid, answer)
        else:
            start = mid + 1
    return answer


print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
