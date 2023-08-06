# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_day = sum([days[month] for month in range(a)]) + b
    return answer[total_day % 7]


print(solution(5, 24))
# 1일 -> 금
# 2 토
# 3 일
# 4월
# 5화
# 6수
# 7목
