# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    def distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    answer = ''
    left_pos = [0, 3]
    right_pos = [2, 3]
    middle_pos = {2: 0, 5: 1, 8: 2, 0: 3}
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_pos = [0, (number - 1) // 3]
        elif number in [3, 6, 9]:
            answer += 'R'
            right_pos = [0, (number // 3) - 1]
        else:
            left_pos_distance = distance(left_pos, [1, middle_pos[number]])
            right_pos_distance = distance(right_pos, [1, middle_pos[number]])
            if left_pos_distance > right_pos_distance:
                answer += 'R'
                right_pos = [1, middle_pos[number]]
            elif left_pos_distance < right_pos_distance:
                answer += 'L'
                left_pos = [1, middle_pos[number]]
            else:
                if hand == "right":
                    answer += 'R'
                    right_pos = [1, middle_pos[number]]
                else:
                    answer += 'L'
                    left_pos = [1, middle_pos[number]]
    return answer

# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #


# "LRLLLRLLRRL"
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
