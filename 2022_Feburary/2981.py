import sys
import math

t = int(input())
arr : list = [] 
res : list = []
gcd = 0

for i in range(t):
    arr.append(int(input()))
    if i == 1:
        gcd = abs(arr[1]-arr[0])
    gcd = math.gcd(abs(arr[i]-arr[i-1]),gcd)

for i in range(2,int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        res.append(i)
        res.append(gcd//i)
res.append(gcd)
res = list(set(res))
res.sort()
for i in res:
    print(i, end = " ")