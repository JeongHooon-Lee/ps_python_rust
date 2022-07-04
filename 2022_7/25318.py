import sys

N = int(input())
datas: list = []
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
years = [365, 366, 365]  # 2019, 2020, 2021,
for i in range(N):
    input_ = list(sys.stdin.readline().strip().split())
    datas.append(input_)
if N == 0:
    print(0)
    exit()
res = 0
p: list = []


def datediff(day: list) -> int:
    hours = int(day[1][0:2])*3600
    minute = int(day[1][3:5])*60
    seconds = int(day[1][6:8]) + hours + minute
    year = sum(years[0:int(day[0][0:4])-2019])
    month = sum(months[0:int(day[0][5:7])-1])
    days = int(day[0][8:10])-1
    total_day = year + month + days + seconds / (3600*24)
    if 2020 == int(day[0][0:4]) and int(day[0][5:7]) >= 3:
        total_day += 1
    return total_day


for i in range(N):
    temp = (datediff(input_)-datediff(datas[i]))/365
    # temp2 = max(0.5**(temp), 0.9**(N-i-1))
    p.append(max(0.5**(temp), 0.9**(N-i-1)))
    # temp3 = p[i] * int(datas[i][-1])
    res += p[i] * int(datas[i][-1])
print(round(res / sum(p)))
