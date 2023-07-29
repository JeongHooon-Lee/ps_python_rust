# https://school.programmers.co.kr/learn/courses/30/lessons/172928


def is_valid_move(park, map_size, direction, distance, current):
    pos = current
    temp = []
    if direction == 'S':
        temp = [1, 0]
    elif direction == 'N':
        temp = [-1, 0]
    elif direction == 'E':
        temp = [0, 1]
    else:
        temp = [0, -1]

    for _ in range(int(distance)):
        pos = [pos[0] + temp[0], pos[1] + temp[1]]
        if not (0 <= pos[0] < map_size[0] and 0 <= pos[1] < map_size[1]):
            return current
        if park[pos[0]][pos[1]] == 'X':
            return current
    return pos


def solution(park, routes):
    map_size = [len(park), len(park[0])]
    current = [0, 0]
    for i in range(map_size[0]):
        if 'S' in park[i]:
            current = [i, park[i].index('S')]
    for order in routes:
        direction, distance = order.split()
        current = is_valid_move(park, map_size, direction, distance, current)
    return current


print(solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]))
