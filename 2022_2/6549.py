import sys

while True:
    arr = sys.stdin.readline().strip()
    arr = list(map(int, arr.split(" ")))
    N = arr[0]
    if N == 0:
        break
    arr = arr[1:]
    
    stack : list = []
    area = 0

    for i in range(len(arr)):
        if not stack:
            stack.append(i)
            continue
        while stack and arr[stack[-1]] > arr[i]:
            temp = stack.pop()
            if not stack:
                area = max(i * arr[temp], area)
            else:
                area = max( (i - stack[-1] - 1) * arr[temp] , area)
        stack.append(i)
    while stack:
        temp = stack.pop()
        if not stack:
            area = max(N * arr[temp], area )
        else:
            area = max( (N-stack[-1]-1) * arr[temp], area)
    print(area)