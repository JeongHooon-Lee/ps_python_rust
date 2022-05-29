import sys

N = int(input())
M = int(input())
union = [i for i in range(N+1)]


def find_parents(vertex):
    if vertex != union[vertex]:
        union[vertex] = find_parents(union[vertex])
    return union[vertex]


def union_(v1, v2):
    parents1 = find_parents(v1)
    parents2 = find_parents(v2)
    if parents1 != parents2:
        union[parents1] = union[parents2] = min(parents1, parents2)


for i in range(1, N+1):
    datas = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(datas)+1):
        if datas[j-1] == 1:
            union_(i, j)

tour_list = list(map(int, sys.stdin.readline().split()))
print(union)
result = union[tour_list[0]]
for i in tour_list:
    if result != union[i]:
        print("NO")
        exit()
print("YES")
