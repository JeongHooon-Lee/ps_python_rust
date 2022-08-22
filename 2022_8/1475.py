import sys

data = sys.stdin.readline().strip()
dict = {i: 0 for i in range(9)}

for i in data:
    if i != "6" and i != "9":
        dict[int(i)] += 1
    else:
        dict[6] += 0.5
res = max(dict.values())

if res == dict[6] and int(res) != res:
    print(int(res)+1)
else:
    print(int(res))
