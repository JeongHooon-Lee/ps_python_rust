# https://school.programmers.co.kr/learn/courses/30/lessons/131128
def solution(X, Y):
    answer = ''
    count = {i: 0 for i in range(10)}
    for i in range(10):
        count[i] += min(X.count(str(i)), Y.count(str(i)))

    answer = ''.join(str(i) * count[i]
                     for i in range(9, -1, -1) if count[i] != 0)
    if not answer:
        return "-1"
    elif answer[0] == '0':
        return "0"
    return answer

# timeout
# def solution(X, Y):
#     answer = ''
#     count = {i: 0 for i in range(10)}
#     for i in range(10):
#         count[i] += min(X.count(str(i)), Y.count(str(i)))

#     answer = ''.join(str(i) * count[i]
#                      for i in range(9, -1, -1) if count[i] != 0)
#     if not answer:
#         return "0"
#     return str(int(answer))
