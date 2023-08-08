import sys

str = sys.stdin.readline().strip()
length = len(str)
if length % 2 == 1:
    str = str[:length//2] + str[length//2 + 1:]
    length -= 1
print(1 if str[:length//2] == str[length - 1:length//2 - 1:-1] else 0)
