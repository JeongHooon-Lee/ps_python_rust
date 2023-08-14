import sys

N = int(input())
h_list = []
result = 0
for i in range(N):
    chat = input().strip()
    if chat == "ENTER":
        h_list = list(set(h_list))
        result += len(h_list)
        h_list = []
    else:
        h_list.append(chat)

print(result + len(list(set(h_list))))
