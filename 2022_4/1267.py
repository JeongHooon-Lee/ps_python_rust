import sys

N = int(input())
y_res = 0
m_res = 0
arr = list(map(int, sys.stdin.readline().split()))
for i in arr:
    y_res += (i//30+1)*10
    m_res += (i//60+1)*15
if y_res == m_res:
    print("Y"+" M " + str(y_res))
elif y_res < m_res:
    print("Y "+str(y_res))
else:
    print("M "+str(m_res))
