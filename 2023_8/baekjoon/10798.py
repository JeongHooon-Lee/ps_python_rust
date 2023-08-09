import sys

answer = [''] * 15
for i in range(5):
    str = list(sys.stdin.readline().strip())
    for j in range(len(str)):
        answer[j] += str[j]
print(''.join(answer))
