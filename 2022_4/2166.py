import sys

N = int(sys.stdin.readline())
list_of_input = []
res = 0
for i in range(N):
    list_of_input.append(list(map(int, sys.stdin.readline().split())))

list_of_input.append(list_of_input[0])

for i in range(len(list_of_input)-1):
    res += (list_of_input[i][0] * list_of_input[i+1][1]) - \
        (list_of_input[i][1] * list_of_input[i+1][0])

print(round(abs(res)/2, 2))
# 0 0
# 0 10
# 10 10
# 10 0


# 0 + -90 + -100 -10
