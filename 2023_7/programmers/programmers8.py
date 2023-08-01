# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    def expriedDate(date: list, target):
        date[1] += target
        date[0] += date[1] // 12
        date[1] = date[1] % 12
        if date[1] % 12 == 0:
            date[0] -= 1
            date[1] = 12
        return date

    def compareDate(date1, date2):
        if date1[0] > date2[0] or (date1[0] == date2[0] and date1[1] > date2[1]) or (date1[0] == date2[0] and date1[1] == date2[1] and date1[2] >= date2[2]):
            return True

    today = list(map(int, today.split('.')))
    term_info: dict = {}
    answer = []

    for i in terms:
        alpha, data = i.split()
        term_info[alpha] = int(data)

    for i in range(len(privacies)):
        date, term = privacies[i].split()
        date = list(map(int, date.split('.')))
        target = term_info[term]
        if compareDate(today, expriedDate(date, target)):
            answer.append(i+1)
    return answer
