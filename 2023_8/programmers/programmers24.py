# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    from itertools import combinations

    return sorted(list(set([sum(i) for i in combinations(numbers, 2)])))


# [2, 3, 4, 5, 6, 7]
print(solution([2, 1, 3, 4, 1]))
