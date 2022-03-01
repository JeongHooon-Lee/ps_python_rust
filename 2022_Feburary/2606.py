#https://www.acmicpc.net/problem/2606
import sys
sys.setrecursionlimit(10**6)

def check_virus(inx):
    if not virused[inx]:
        virused[inx] = 1
    if len(network[inx]) == 0:
        return 
    else:
        for i in network[inx]:
            if virused[i] != 1:
                check_virus(i)

computer = int(input().strip())
n = int(sys.stdin.readline())
network = [ [] for _ in range(101) ]
virused = [ 0 for _ in range(101) ]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)
#print(network)
check_virus(1)
print(virused.count(1)-1)
    