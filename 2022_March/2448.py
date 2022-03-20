import sys

N = int(sys.stdin.readline())
N //= 3
cnt =0
while N > 1:
    N //= 2
    cnt +=1

tri = ["  *  "," * * ","*****"]
def maketree():
    lenth = len(tri)
    for i in range(lenth):
        tri.append(tri[i] + " " + tri[i])
        tri[i] = " "*lenth + tri[i] + " "*lenth

for i in range(cnt):
    maketree()

for i in tri:
    print(i)