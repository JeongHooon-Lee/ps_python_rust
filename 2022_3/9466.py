import sys
sys.setrecursionlimit(10**6)
def dfs(target):
    global res
    visited[target] = True
    cycle.append(target)

    if visited[student_pick[target]]:
        if student_pick[target] in cycle:
            res += cycle.index(student_pick[target])
        else:
            res += len(cycle)
        return
    else:
        dfs(student_pick[target])
        
for _ in range(int(input())):
    number_of_student = int(sys.stdin.readline())
    visited = [False]*(number_of_student+1)
    res = 0
    student_pick = [-1]+ list(map(int, sys.stdin.readline().split()))
    
    for i in range(1, number_of_student+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(res)