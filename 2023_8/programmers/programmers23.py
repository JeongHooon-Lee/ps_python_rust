# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    def step1(str):
        return str.lower()

    def step2(str):
        return "".join(list(map(lambda x: x if x == '-' or x == '_' or x == '.' or (97 <= ord(x) <= 122) or (48 <= ord(x) <= 57) else '', str)))

    def step3(str):
        if not str:
            return ""
        result = str[0]
        for i in str[1:]:
            if i == '.' and result[-1] == '.':
                continue
            result += i
        return result

    def step4(str):
        if not str:
            return ""
        if str[0] == '.':
            str = str.replace('.', '', 1)
        if str and str[-1] == '.':
            str = str[:-1]
        return str

    def step5(str):
        if not str:
            return 'a'
        return str

    def step6(str):
        if len(str) > 15:
            str = str[:15]
            if str[-1] == ".":
                str = str[:-1]
        return str

    def step7(str):
        if len(str) <= 2:
            for i in range(3 - len(str)):
                str += str[-1]
        return str

    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)
    return new_id


print(solution("abcdefghijklmn.p"))
