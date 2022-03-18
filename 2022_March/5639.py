import sys
sys.setrecursionlimit(10**6)
preorder_tree = []

while True:
    try:
        temp = int(input())
        preorder_tree.append(temp)
    except:
        break


def postorder(tree):
    if len(tree) == 1 or len(tree) == 0:
        return tree
    root = tree[0]
    right_tree = len(tree)
    for i in range(len(tree)):
        if tree[i] > root:
            right_tree = i
            break
    return postorder(tree[1:right_tree])+postorder(tree[right_tree:])+[root]
for i in postorder(preorder_tree):
    print(i)