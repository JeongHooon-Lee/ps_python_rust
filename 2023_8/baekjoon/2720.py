import sys

t = int(input())

money = [25, 10, 5, 1]
for _ in range(t):
    answer = []
    c = int(input())

    for m in money:
        answer.append(c//m)
        c %= m

    print(*answer)
