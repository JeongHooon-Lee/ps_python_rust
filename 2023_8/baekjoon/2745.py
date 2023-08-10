import sys

N, B = sys.stdin.readline().split()

answer = 0
for inx in range(len(N)):
    ch = N[-1 * (inx + 1)]
    if ch.isalpha():
        answer += int(B) ** inx * (ord(ch) - 55)
    else:
        answer += int(B) ** inx * int(ch)
print(answer)
