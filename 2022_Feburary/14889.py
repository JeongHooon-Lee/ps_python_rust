from itertools import combinations
import sys

N = int(input().strip())
array : list = []
members = [ i for i in range(N) ]
possible = []
answer = 100000

for team in list(combinations(members,N//2)):
    possible.append(team)

for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(possible)//2):
    team = possible[i]
    stat_A = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_A += array[member][k]

    team = possible[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += array[member][k]
    
    answer = min(answer,abs(stat_A-stat_B))


print(answer)