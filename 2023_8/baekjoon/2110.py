N, C = map(int, input().split())
router = []
for i in range(N):
    router.append(int(input()))
router.sort()
result = 0


def solution(start, end) -> int:
    while start <= end:
        count = 1
        mid = (start + end) // 2
        last_router_pos = router[0]

        for i in range(1, N):
            if router[i] - last_router_pos >= mid:
                count += 1
                last_router_pos = router[i]

        if count >= C:
            global result
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


print(solution(1, router[-1] - router[0]))
