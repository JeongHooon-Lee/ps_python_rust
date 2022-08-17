import sys

datas = list(sys.stdin.readline().split())
mon = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
       "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
       7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
month = datas[0]
dd = int(datas[1][:-1])-1
yy = int(datas[2])
hh = int(datas[3][0:2])
mm = int(datas[3][-2:])
total = 365*24*60
if not (yy % 400) or ((yy % 4 == 0) and (yy % 100 != 0)):
    day[2] += 1
    total += 24*60
days = dd
for i in range(1, mon[month]):
    days += day[i]
total_min = days*24*60 + int(hh)*60 + mm

print(total_min/total * 100)
