# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    report_list = {id: [0, set()] for id in id_list}
    for info in report:
        frm, target = info.split()
        report_list[target][1].add(frm)
    for id in id_list:
        if len(report_list[id][1]) >= k:
            for reporter in report_list[id][1]:
                report_list[reporter][0] += 1
    return [i[0] for i in report_list.values()]


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
