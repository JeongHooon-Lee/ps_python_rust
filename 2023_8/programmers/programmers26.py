# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)

    for move in moves:
        for i in range(N):
            doll = board[i][move - 1]

            if doll != 0:
                board[i][move - 1] = 0

                if stack and stack[-1] == doll:
                    answer += 2
                    stack.pop()
                    break

                stack.append(doll)
                break

    return answer


# 4
print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
