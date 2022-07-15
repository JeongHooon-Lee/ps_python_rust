import sys

king, stone, N = sys.stdin.readline().strip().split()
king = [ord(king[0])-65, int(king[1])]
stone = [ord(stone[0])-65, int(stone[1])]
oper = {'B': [0, -1], 'L': [-1, 0], 'R': [1, 0], 'T': [0, 1],
        'LB': [-1, -1], 'LT': [-1, 1], 'RB': [1, -1], 'RT': [1, 1]}


def move(op):
    global king, stone
    nx, ny, sx, sy = 0, 0, 0, 0
    nx = king[0] + oper[op][0]
    ny = king[1] + oper[op][1]
    if 0 <= nx < 8 and 0 < ny <= 8:
        sx = stone[0] + oper[op][0]
        sy = stone[1] + oper[op][1]
        if nx == stone[0] and ny == stone[1]:
            if 0 <= sx < 8 and 0 < sy <= 8:
                king = [nx, ny]
                stone = [sx, sy]
        else:
            king = [nx, ny]


for i in range(int(N)):
    data = sys.stdin.readline().strip()
    move(data)
king[0] = chr(king[0]+65)
stone[0] = chr(stone[0]+65)
king[1] = str(king[1])
stone[1] = str(stone[1])
print("".join(king))
print("".join(stone))
