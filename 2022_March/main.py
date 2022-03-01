import sys

board = []
for i in range(9):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)

print(board[:3][:3])
print(board[3][:3])