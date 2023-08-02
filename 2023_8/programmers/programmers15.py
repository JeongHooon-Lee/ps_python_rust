# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    stack = []
    answer = 0
    for v in ingredient:
        stack.append(v)
        if len(stack) >= 4 and stack[-1] == 1 and stack[-4::] == [1, 2, 3, 1]:
            for _ in range(4):
                stack.pop()
            answer += 1
    return answer


print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
