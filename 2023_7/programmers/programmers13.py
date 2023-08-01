# https://school.programmers.co.kr/learn/courses/30/lessons/135808
# import heapq


# def solution(k, m, score):
#     answer = 0
#     heap = [-v for v in score]
#     heapq.heapify(heap)
#     while True:
#         if len(heap) < m:
#             break
#         arr = []
#         for _ in range(m):
#             arr.append(-1 * heapq.heappop(heap))
#         answer += min(arr) * m
#     return answer


def solution(k, m, score):
    return sum(sorted(score)[len(score) % m::m]) * m


print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
