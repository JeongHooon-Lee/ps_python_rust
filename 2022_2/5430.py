import sys
def func(R_count):
    for i in command:
        if i == "R":
            R_count +=1
        elif i == "D":
            if len(numbers) == 0:
                return("error")
            if R_count%2 == 1:
                del numbers[-1]
            elif R_count%2 == 0:
                del numbers[0]

    if R_count%2 == 1:
        numbers.reverse()
    return(numbers)

answer = []
for i in range(int(sys.stdin.readline())):
    R_count = 0
    command = list("".join(list(sys.stdin.readline().strip())))
    n = int(sys.stdin.readline())
    numbers = [ x for x in sys.stdin.readline().strip()[1:-1].split(",") if x.isdigit() ]
    
    temp = func(R_count)
    if temp == "error":
        print(temp)
    else:
        print("["+",".join(temp)+"]")
