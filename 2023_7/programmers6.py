# https://school.programmers.co.kr/learn/courses/30/lessons/159994
def solution(cards1, cards2, goal):
    for word in goal:
        if cards1 and cards1[0] == word:
            cards1 = cards1[1:]
            goal = goal[1:]
        elif cards2 and cards2[0] == word:
            cards2 = cards2[1:]
            goal = goal[1:]
    return 'Yes' if not goal else 'No'


print(solution(["a", "b", "c"], ["d", "e", "f"], ["a", "d", "f"]))
