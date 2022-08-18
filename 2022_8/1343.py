import sys

datas = sys.stdin.readline().strip()

head = 0
res = ""
while head < len(datas):
    if datas[head] == ".":
        head += 1
        res += "."
        continue
    else:
        if head <= len(datas)-3 and datas[head:head+4] == "XXXX":
            res += "AAAA"
            head += 4
        elif head <= len(datas)-1 and datas[head:head+2] == "XX":
            res += "BB"
            head += 2
        else:
            print(-1)
            break

if head >= len(datas):
    print(res)
