import sys

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())


def find_value(y, x):
    rotate = max(abs(y), abs(x))+1
    if rotate == 1:
        return 1
    else:
        min_num = (1 + (rotate - 2) * 2)**2+1
        max_num = (1 + (rotate - 1) * 2)**2
        if y == -(rotate-1) or (x == (rotate-1) and y != (rotate-1)):
            return min_num + (rotate-2 - y) + (rotate-1 - x)
        else:
            return max_num - (rotate-1-y) - (rotate-1-x)


temp = max(len(str(find_value(r1, c1))), len(str(find_value(r2, c2))))

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print("%*d" % (temp, find_value(i, j)), end=' ')
    print()
