# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    student = {i: 1 for i in range(1, n + 1)}
    for i in range(1, n + 1):
        if i in lost:
            student[i] -= 1
        if i in reserve:
            student[i] += 1

    if student[1] == 0 and student[2] == 2:
        student[1] = student[2] = 1
    for i in range(2, n):
        if student[i] == 0:
            if student[i - 1] == 2:
                student[i] = student[i - 1] = 1
            elif student[i + 1] == 2:
                student[i] = student[i + 1] = 1
    if student[n] == 0 and student[n - 1] == 2:
        student[n - 1] = student[n] = 1

    return sum(1 for i in student.values() if i > 0)


# 5
print(solution(3, [3], [1]))
