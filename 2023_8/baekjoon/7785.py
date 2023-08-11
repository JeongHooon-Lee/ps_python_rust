import sys

n = int(input())

dict = {}
for i in range(n):
    name, status = sys.stdin.readline().split()
    if status == "enter":
        dict[name] = 1
    else:
        dict.pop(name)

for n in sorted(dict, reverse=True):
    print(n)
