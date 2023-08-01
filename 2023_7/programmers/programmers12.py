# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    def count(n):
        c = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                c += 2
                if i == n ** 0.5:
                    c -= 1
        return c
    arr = [count(n) if count(n) <=
           limit else power for n in range(1, number + 1)]

    return sum(arr)


print(solution(10, 3, 2))
