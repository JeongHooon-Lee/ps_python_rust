
# [2 3 4 5], [9 14], [7, 12, ]
# 각자, 합, 차,

# 2 5 9 14
import sys

N = int(input())
datas = list(map(int, sys.stdin.readline().split()))
res = set()

for data in datas:
    temp_s = set()
    for value in res:
        temp_s.add(data + value)
        temp_s.add(abs(data - value))
    temp_s.add(data)
    res |= temp_s

N = int(input())
testcases = list(map(int, sys.stdin.readline().split()))

result = []
for testcase in testcases:
    result.append("Y" if testcase in res else "N")
print(*result)
