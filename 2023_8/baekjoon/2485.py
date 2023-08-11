N = int(input())

trees = []
spaces = []
for i in range(N):
    trees.append(int(input()))
    spaces.append(trees[i] - trees[i - 1])
gcd = spaces[1]


def get_gcd(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)

    while a % b != 0:
        a, b = b, a % b
    return b


for space in spaces[2:]:
    gcd = get_gcd(gcd, space)

print((trees[-1] - trees[0]) // gcd + 1 - len(trees))


# 1
# 3
# 5
