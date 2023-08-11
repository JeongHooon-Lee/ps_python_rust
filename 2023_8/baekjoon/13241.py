A, B = map(int, input().split())
A, B = min(A, B), max(A, B)


def get_divisor(n: int):
    if n == 1:
        return [1]
    divisor = [1, n]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if n // i != i:
                divisor.append(i)
    return sorted(divisor, reverse=True)


divisor = get_divisor(A)

for div in divisor:
    if B % div == 0:
        print(A*B//div)
        break
# 6 8 24

# 3 4
# 2 2
# 1 1
