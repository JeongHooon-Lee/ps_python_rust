while True:
    N = int(input())
    if N == -1:
        break
    divisor = [1]

    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            divisor.append(i)
            if N // i != i:
                divisor.append(N // i)
    divisor.sort()

    if sum(divisor) == N:
        print("{} = {}".format(N, " + ".join(map(str, divisor))))
    else:
        print("{} is NOT perfect.".format(N))
