import sys

x, y = map(int, sys.stdin.readline().split())

for i in range(1,x):
    if i in [1,3,5,7,8,10,12]:
        y += 31
    elif i in [4,6,9,11]:
        y += 30
    else:
        y += 28
temp = y%7
if temp == 1:
    print("MON")
elif temp == 2:
    print("TUE")
elif temp == 3:
    print("WED")
elif temp == 4:
    print("THU")
elif temp == 5:
    print("FRI")
elif temp == 6:
    print("SAT")
elif temp == 0:
    print("SUN")