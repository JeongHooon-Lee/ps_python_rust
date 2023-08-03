# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    nums = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4',
            "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    for num in nums:
        s = s.replace(num, nums[num])
    return int(s)


print(solution("23four5six7"))
