
def is_prime(n: int) -> int:
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True


def find_next_one(n: int) -> int:
    while True:
        if is_prime(n) == True:
            return n
        n += 1


t = int(input())

for _ in range(t):
    answer = find_next_one(int(input()))

    print(answer)
