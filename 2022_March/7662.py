import sys
import heapq

for i in range(int(input())):
    N = int(sys.stdin.readline())
    max_hque = []
    min_hque = []
    visited = [False]*N

    for j in range(N):
        a = sys.stdin.readline().strip().split()
        if a[0] == "I":
            heapq.heappush(max_hque, (-int(a[1]),j))
            heapq.heappush(min_hque, (int(a[1]),j))
            visited[j] = True
        elif a[0] == "D":
            if a[1] == "-1":
                while min_hque and not visited[min_hque[0][1]]:
                    heapq.heappop(min_hque)
                if min_hque:
                    visited[min_hque[0][1]] = False
                    heapq.heappop(min_hque)

            elif a[1] == "1":
                while max_hque and not visited[max_hque[0][1]]:
                    heapq.heappop(max_hque)
                if max_hque:
                    visited[max_hque[0][1]] = False
                    heapq.heappop(max_hque)
    
    while min_hque and not visited[min_hque[0][1]]:
        heapq.heappop(min_hque)
    while max_hque and not visited[max_hque[0][1]]:
        heapq.heappop(max_hque)

    if not max_hque:
        print("EMPTY")
    elif max_hque and min_hque:
        print(-heapq.heappop(max_hque)[0],heapq.heappop(min_hque)[0])