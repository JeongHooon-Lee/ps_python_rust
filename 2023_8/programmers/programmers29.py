# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    result = [0, 0, 0]
    second_arr = [5, 1, 3, 4, 5]
    third_arr = [5, 3, 3, 1, 1, 2, 2, 4, 4, 5]
    for inx in range(1, len(answers) + 1):
        first = inx % 5 if inx % 5 != 0 else 5
        second = second_arr[(inx % 8) // 2] if inx % 2 == 0 else 2
        third = third_arr[(inx) % 10]
        if answers[inx - 1] == first:
            result[0] += 1
        if answers[inx - 1] == second:
            result[1] += 1
        if answers[inx - 1] == third:
            result[2] += 1

    return [i + 1 for i in range(3) if result[i] == max(result)]
