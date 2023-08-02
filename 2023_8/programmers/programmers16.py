# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    pronunciation = ["aya", "ye", "woo", "ma"]
    babbling = [v for v in babbling if not any(
        (pron * 2) in v for pron in pronunciation)]

    answer = 0
    for v in babbling:
        for pron in pronunciation:
            v = v.replace(pron, " ")
        if v.isspace():
            answer += 1
    return answer


print(solution(["aya", "yee", "u", "maa"]))
