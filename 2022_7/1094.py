import heapq

X = int(input())
datas = []
heapq.heappush(datas, 64)
count = 1

while True:
    if sum(datas) > X:
        temp = heapq.heappop(datas)
        if temp // 2 + sum(datas) >= X:
            heapq.heappush(datas, temp//2)
        else:
            for i in range(2):
                heapq.heappush(datas, temp//2)
    else:
        break

print(len(datas))
