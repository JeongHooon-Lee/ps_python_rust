import sys

data = sys.stdin.readline().strip()
dictionary: dict = {}
even: list = []
odd: list = []
for i in data:
    try:
        dictionary[i] += 1
    except:
        dictionary[i] = 1

for i in dictionary.keys():
    if dictionary[i] % 2 == 0:
        even.append((i, dictionary[i]//2))
    else:
        even.append((i, dictionary[i]//2))
        odd.append((i, dictionary[i]))
even.sort()
odd.sort()

if len(data) % 2 == 0:
    if len(odd) != 0:
        print("I\'m Sorry Hansoo")
    else:
        temp = [a*b for a, b in even]
        print("".join(map(str, temp + temp[::-1])))
else:
    if len(odd) != 1:
        print("I\'m Sorry Hansoo")
    else:
        temp = [a*b for a, b in even]
        print("".join(map(str, temp + [odd[0][0]] + temp[::-1])))
