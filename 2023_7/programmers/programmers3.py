# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    answer = [51, 51, 0, 0]
    map_size = [len(wallpaper), len(wallpaper[0])]
    for line in range(map_size[0]):
        for c in range(map_size[1]):
            if wallpaper[line][c] == '#':
                answer[0] = min(answer[0], line)
                answer[1] = min(answer[1], c)
                answer[2] = max(answer[2], line + 1)
                answer[3] = max(answer[3], c + 1)
    return answer


print(solution(["..", "#."]))
