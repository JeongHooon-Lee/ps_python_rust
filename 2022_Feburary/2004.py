import sys
a, b = map(int, sys.stdin.readline().split())

def count_two(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer

def count_five(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

print(min(count_two(a)-count_two(a-b)-count_two(b),count_five(a)-count_five(a-b)-count_five(b)))