import sys

n = int(input().strip())
answer : int = 0
row = [0] * n

def Check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

def Queens(x):
    global answer
    if x == n:
        answer +=1

    else:
        for i in range(n):
            row[x] = i
            if Check(x):
                Queens(x+1)

Queens(0)
print(answer)