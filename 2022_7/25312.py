import sys
from fractions import Fraction

N, M = map(int, sys.stdin.readline().split())
datas: list = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    datas.append((v/w, Fraction(v, w), w, v))
current = M
res = 0
datas.sort(reverse=True)

for ratio, frac, total, sugar in datas:
    if current >= total:
        res += sugar
        current -= total
    else:
        res += frac*current
        break
res = str(res)
try:
    if int(res):
        print(res+"/1")
except:
    print(res)
