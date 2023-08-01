# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    dict = {n: y for n, y in zip(name, yearning)}
    res = []
    for given in photo:
        buf = 0
        for key in given:
            if key in dict:
                buf += dict[key]
        res.append(buf)
    return res


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [
      ["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
