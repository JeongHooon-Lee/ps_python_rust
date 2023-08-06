# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):

    def is_prime(number):
        for num in range(2, int(number ** (0.5)) + 1):
            if number % num == 0:
                return False
        return True

    answer = 1
    for i in range(3, n + 1):
        if is_prime(i):
            answer += 1

    return answer


print(solution(10))
