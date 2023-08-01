# https://school.programmers.co.kr/learn/courses/30/lessons/160586
def solution(keymap, targets):
    dict = {chr(x): 101 for x in range(ord('A'), ord('A') + 26)}
    answer = []
    for button in keymap:
        for index in range(len(button)):
            dict[button[index]] = min(dict[button[index]], index + 1)
    for target in targets:
        buf = []
        for ch in target:
            if dict[ch] != 101:
                buf.append(dict[ch])
        if len(buf) != len(target):
            answer.append(-1)
        else:
            answer.append(sum(buf))
    return answer


print(solution(["BC"], ["AC", "BC"]))
