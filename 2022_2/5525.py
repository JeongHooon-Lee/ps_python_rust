import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

answer =0
i=0
pattern=0
while True:
    if i >= M-2:
        break
    if S[i] == "I" and S[i+1] == "O" and S[i+2] == "I":
        pattern +=1
        if pattern == N:
            pattern -=1
            answer +=1
        i+=1
    else:
        pattern=0
    i+=1
print(answer)
