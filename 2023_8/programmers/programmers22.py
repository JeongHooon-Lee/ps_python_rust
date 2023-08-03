# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    result = [0, 0]
    # 0~6가지 나올 수 있음
    match = len(set(lottos).intersection(set(win_nums)))
    # 6-match 가지 나올 수 있음
    zeros = lottos.count(0)
    result[0] = 7 - (match + zeros) if match > 0 or zeros > 0 else 6
    result[1] = 7 - match if match >= 2 else 6
    return result


print(solution([45, 4, 35, 20, 3, 9], 	[20, 9, 3, 45, 4, 35]))
