import sys
from itertools import combinations


def get_relation(arr: list[str]):
    return compare(arr[0], arr[1]) \
        + compare(arr[1], arr[2]) \
        + compare(arr[0], arr[2])


def compare(a: str, b: str):
    result = 0
    for c1, c2 in zip(a, b):
        if c1 != c2:
            result += 1

    return result


for i in range(int(input())):
    result = sys.maxsize
    N = int(input())
    mbti = list(input().split(" "))
    arr = []
    mbti_count = {'ISTJ': 0, 'ISFJ': 0, 'INFJ': 0, 'INTJ': 0,
                  'ISTP': 0, 'ISFP': 0, 'INFP': 0, 'INTP': 0,
                  'ESTP': 0, 'ESFP': 0, 'ENFP': 0, 'ENTP': 0,
                  'ESTJ': 0, 'ESFJ': 0, 'ENFJ': 0, 'ENTJ': 0}
    for i in mbti:
        if mbti_count[i] < 3:
            arr.append(i)
            mbti_count[i] += 1
    for a, b, c in combinations(arr, 3):
        buf = get_relation([a, b, c])
        result = buf if result > buf else result
    print(result)
