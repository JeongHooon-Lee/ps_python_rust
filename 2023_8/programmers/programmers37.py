# https://school.programmers.co.kr/learn/challenges?order=recent&statuses=unsolved&levels=1&languages=python3

def solution(nums):
    length = len(nums) // 2
    unique = len(set(nums))
    return min(length, unique)


print(solution([3, 3, 3, 2, 2, 2]))
