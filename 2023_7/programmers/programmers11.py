# https://school.programmers.co.kr/learn/courses/30/lessons/138477
import heapq


def solution(k, score):
    answer = []
    heap = []
    for v in score:
        if len(heap) != k:
            heapq.heappush(heap, v)
        else:
            if min(heap) < v:
                heapq.heappop(heap)
                heapq.heappush(heap, v)
        answer.append(min(heap))
    return answer


print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
