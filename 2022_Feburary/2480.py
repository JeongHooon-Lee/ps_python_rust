import sys

numbers = list(map(int, sys.stdin.readline().split()))

if numbers.count(numbers[0]) == 3:
    print(10000+numbers[0]*1000)
elif numbers.count(numbers[0]) == 2:
    print(1000+numbers[0]*100)
elif numbers.count(numbers[1]) == 2:
    print(1000+numbers[1]*100)
else:
    print(max(numbers)*100)

