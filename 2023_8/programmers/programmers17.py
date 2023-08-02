# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0

    while n >= a:
        answer += (n // a) * b
        n = n % a + (n // a) * b
    return answer


# answer += n // a
# n = n % a + n // a

# 10 + 5 + 2 + 1 + 1

# 10, 5,   3,  2,  1

print(solution(4, 1, 20))
