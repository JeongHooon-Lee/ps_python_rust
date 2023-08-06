# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations


def solution(nums):

    def is_prime(number):
        for num in range(2, int(number ** (0.5)) + 1):
            if number % num == 0:
                return False
        return True

    answer = 0
    for i in combinations(nums, 3):
        if is_prime(sum(i)):
            answer += 1

    return answer


print(solution([1, 2, 7, 6, 4]))
