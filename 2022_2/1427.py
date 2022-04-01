import sys

s = sys.stdin.readline().strip()

s=list(map(int, "".join(s)))
s.sort(reverse=1)
for i in s:
    print(i,end='')