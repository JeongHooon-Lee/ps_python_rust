# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    dict = {}
    for part in participant:
        if part in dict:
            dict[part] += 1
        else:
            dict[part] = 1

    for com in completion:
        dict[com] -= 1

    return ''.join([key for key in dict if dict[key] == 1])


print(solution(["kiki", "kiki", "kiki"], ["kiki", "kiki"]))
