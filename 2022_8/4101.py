import sys

while True:
    data = sys.stdin.readline().strip()
    res = 0
    data = data.lower()
    if data == "#":
        break
    res += data.count("a")
    res += data.count("e")
    res += data.count("i")
    res += data.count("o")
    res += data.count("u")
    print(res)
