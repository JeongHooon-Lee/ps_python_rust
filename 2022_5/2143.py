import sys

T = int(input())
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
M = int(input())
B = list(map(int, sys.stdin.readline().split()))

A_data = []
for i in range(N):
    for j in range(i, N):
        A_data.append(sum(A[i:j+1]))


B_data = []
for i in range(M):
    for j in range(i, M):
        B_data.append(sum(B[i:j+1]))
A_data.sort()
B_data.sort(reverse=True)
A_len = len(A_data)
B_len = len(B_data)

left = right = res = 0

while left < A_len and right < B_len:
    if A_data[left] + B_data[right] == T:
        temp1 = temp2 = 1
        left += 1
        right += 1
        while left < A_len and A_data[left] == A_data[left-1]:
            left += 1
            temp1 += 1
        while right < B_len and B_data[right] == B_data[right-1]:
            right += 1
            temp2 += 1
        res += temp1 * temp2

    elif A_data[left] + B_data[right] < T:
        left += 1
    else:
        right += 1
print(res)
