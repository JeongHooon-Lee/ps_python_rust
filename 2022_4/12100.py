from copy import deepcopy
import sys

N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
res = 0


def up(board):
    for i in range(N):
        pointer = 0
        for j in range(1, N):
            if board[j][i]:
                temp = board[j][i]
                board[j][i] = 0
                if board[pointer][i] == 0:
                    board[pointer][i] = temp
                elif board[pointer][i] == temp:
                    board[pointer][i] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[pointer][i] = temp
    return board


def left(board):
    for i in range(N):
        pointer = 0
        for j in range(1, N):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = temp
                elif board[i][pointer] == temp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer] = temp
    return board


def right(board):
    for i in range(N):
        pointer = N-1
        for j in range(N-2, -1, -1):
            if board[i][j]:
                temp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = temp
                elif board[i][pointer] == temp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = temp
    return board


def down(board):
    for i in range(N):
        pointer = N-1
        for j in range(N-2, -1, -1):
            if board[j][i]:
                temp = board[j][i]
                board[j][i] = 0
                if board[pointer][i] == 0:
                    board[pointer][i] = temp
                elif board[pointer][i] == temp:
                    board[pointer][i] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][i] = temp
    return board


def dfs(board, count):
    if count == 5:
        return max(map(max, board))

    return max(dfs(up(deepcopy(board)), count+1), dfs(down(deepcopy(board)), count+1), dfs(right(deepcopy(board)), count+1), dfs(left(deepcopy(board)), count+1))


print(dfs(board, 0))
