# https://school.programmers.co.kr/learn/courses/30/lessons/134240
def solution(food):
    answer = ''
    for inx, f in enumerate(food[1:]):
        answer += str(inx + 1) * (f//2)
    return answer + '0' + answer[::-1]


print(solution([1, 3, 4, 6]))
