import sys

N = int(input())
dic: dict = {}
for i in range(N):
    data = list(sys.stdin.readline().split())
    temp = 0
    res: list = []
    for j in data:
        try:
            dic[j[0]] = 1
            res.append((j, 0))
            flag = 1
            break
        except:
            continue
    if len(res) != i:
        data = [i[1:] for i in data]
        for j in data:
            for k in range(len(j)):
                try:
                    if dic[k] or dic[k.upper()]:
                        continue
                except:
                    dic[k] = 1
                    res.append((j, k))
                    break
            if len(res) == i:
                break
    for j in range(len(data)):
        for k in range(len(data[i])):
            if j == res[0] and k == res[1]:
                print("["+data[i][j]+"]", end='')
            print(data[i][j], end='')
