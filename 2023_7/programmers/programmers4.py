# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 0
    pos = section[0]
    for i in section:
        if pos < i:
            pos = i
            continue
        elif pos > i:
            continue
        pos += m
        answer += 1
    return answer


print(solution(5, 2, [1, 4, 5]))
