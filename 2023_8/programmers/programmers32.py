# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = []
    num = ''
    sdt = ['S', 'D', 'T']

    for dart in ''.join(dartResult):
        if dart.isnumeric():
            num += dart

        elif dart.isalpha():
            answer.append(int(num))
            num = ''
            answer[-1] = answer[-1] ** (sdt.index(dart) + 1)

        else:
            if dart == '*':
                answer[-2:] = [i * 2 for i in answer[-2:]]
            else:
                answer[-1] = answer[-1] * -1
    return sum(answer)


print(solution("1T2D3D#"))
