import sys
N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
is_in = list(map(int, sys.stdin.readline().split()))
cards.sort()
# -10 2 3 6 10
for i in is_in:
    start = 0
    end = N-1
    found = 0
    while start <= end: 
        mid = (start+end)//2
        if cards[mid] == i:
            found = 1 
            break
        elif cards[mid] > i:
            end = mid -1
        elif cards[mid] < i:
            start = mid + 1
    if found == 1:
        print("1",end = " ")
    else:
        print("0",end= " ")