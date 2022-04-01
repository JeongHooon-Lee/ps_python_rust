import sys
sys.setrecursionlimit(10**6)

def moving(fromPos,num,ToPos):
    global counter, arr
    temp = [1,2,3]
    temp.remove(fromPos)
    temp.remove(ToPos)
    temp = temp[0]
    if num == 2:
        arr.append((fromPos, temp))
        arr.append((fromPos, ToPos))
        arr.append((temp, ToPos))
        counter +=3
    else:
        moving(fromPos,num-1,temp)
        arr.append((fromPos, ToPos))
        counter +=1
        moving(temp,num-1,ToPos)

N = int(sys.stdin.readline().strip())
if N == 1:
    print(1)
    print(1,3)
    quit()
counter = 0
arr = []
moving(1,N,3)
print(counter)
for i in arr:
    for j in i:
        print(j,end=" ")
    print()