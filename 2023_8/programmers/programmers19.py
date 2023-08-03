# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    # RT, CF, JM, AN
    length = len(survey)
    kinds = {"RT": 0, "CF": 1, "JM": 2, "AN": 3}
    points = [[0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(length):
        if ''.join(sorted(survey[i])) != survey[i]:
            survey[i] = ''.join(sorted(survey[i]))
            choices[i] = 8 - choices[i]

    for i in range(length):
        kind = kinds[survey[i]]
        if choices[i] > 4:
            points[kind][1] += choices[i] - 4
        elif choices[i] < 4:
            points[kind][0] += 4 - choices[i]
    for i in range(4):
        if points[i][0] < points[i][1]:
            answer += list(kinds.keys())[i][1]
        else:
            answer += list(kinds.keys())[i][0]
    return answer


print(solution(["RT", "RT", "RT"], [7, 2, 4]))
