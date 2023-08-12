def sieve_of_eratosthenes(limit):
    primes = {i: True for i in range(1, limit + 1)}
    primes[1] = False
    # primes = [True] * (limit + 1)
    p = 2
    while p ** 2 <= limit:
        if primes[p]:
            for i in range(p ** 2, limit + 1, p):
                primes[i] = False
        p += 1
    return primes


def goldbach_partitions_count(even_number, primes):
    count = 0
    for prime in primes:
        if not primes[prime]:
            continue
        if prime > even_number // 2:
            break
        if primes[even_number - prime]:
            count += 1
    return count


limit = 1000000  # 충분히 큰 범위의 소수 리스트 생성
primes = sieve_of_eratosthenes(limit)
print([p for p in range(1, limit + 1) if primes[p] == True])
n = int(input())
for _ in range(n):
    even_number = int(input())
    partitions_count = goldbach_partitions_count(even_number, primes)
    print(partitions_count)
