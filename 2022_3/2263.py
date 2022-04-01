import sys

N = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
root = postorder[-1]

def func(inord,psord):
    if len(inord) == 3:
        temp = list(reversed(inord))
        if inord == psord:
            return temp
        elif temp == psord:
            return inord
        else:
            return [inord[1],inord[0],inord[2]]
    elif len(inord) < 3:
        if inord == psord:
            return list(reversed(inord))
        else:
            return inord
            
    root = psord[-1]
    len_of_left = inord.index(root)
    return [root] + func(inord[:len_of_left],psord[:len_of_left]) + func(inord[len_of_left+1:],psord[len_of_left:-1])

print(*func(inorder,postorder))