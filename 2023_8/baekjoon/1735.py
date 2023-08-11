A, B = map(int, input().split())
C, D = map(int, input().split())


E, F = A * D + C * B, B * D

G, H = max(E, F), min(E, F)

while G % H != 0:
    G, H = H, G % H

print(E // H, F // H)
