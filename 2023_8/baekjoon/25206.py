import sys

total_unit = 0
total_score = 0
scores = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
          'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
while True:
    try:
        sub, unit, score = sys.stdin.readline().split()
        if score != 'P':
            total_unit += float(unit)
            total_score += scores[score] * float(unit)
    except:
        print(total_score/total_unit)
        break
