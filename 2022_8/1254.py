import sys

S = sys.stdin.readline().strip()
length = len(S)

for i in range(length):
    if S[i:] == S[i:][::-1]:
        print(len(S)+i)
        break
