N = int(input())
times = []
for _ in range(N):
    s, e = map(int, input().split())
    times.append( (s, e) )
times.sort(key = lambda s: (s[1], s[0]))

result = 0
end_time = 0

for time in times:
    start, end = time[0], time[1]

    if time[0] >= end_time:
        result += 1
        end_time = end
        
print(result)
