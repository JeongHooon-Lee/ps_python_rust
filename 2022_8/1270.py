import sys

N = int(input())
for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    dictionary = {}
    for i in data[1:]:
        try:
            dictionary[i] += 1
        except:
            dictionary[i] = 1
    res = sorted([(dictionary[i], i)
                 for i in dictionary.keys()], key=lambda x: x[0], reverse=True)
    if res[0][0] > data[0]//2:
        print(res[0][1])
    else:
        print("SYJKGW")
