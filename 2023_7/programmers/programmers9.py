# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    dict = {}
    for inx in range(len(s)):
        ch = s[inx]
        if ch not in dict:
            answer.append(-1)
            dict[ch] = inx
        else:
            answer.append(inx - dict[ch])
            dict[ch] = inx
    return answer


print(solution("foobar"))
