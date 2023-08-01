# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    def logic(str):
        x = 1
        y = 0
        target = str[0]
        for inx in range(1, len(str)):
            if str[inx] == target:
                x += 1
            else:
                y += 1

            if x == y:
                return str[inx + 1:]
        return ""

    answer = 0
    while True:
        s = logic(s)
        answer += 1
        if not s:
            break

    return answer


print(solution("aaabbaccccabba"))
