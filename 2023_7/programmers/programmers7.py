# https://school.programmers.co.kr/learn/courses/30/lessons/155652
def solution(s, skip, index):
    answer = ''
    for ch in s:
        temp = ord(ch)
        count = index
        while count:
            temp = temp + 1
            if temp > ord('z'):
                temp = ord('a')
            if chr(temp) in skip:
                continue
            count -= 1
        answer += chr(temp)
    return answer


print(solution("aukks", "wbqd", 5))
