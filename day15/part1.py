import re
input = open("input.txt")

sensors = []
beaconsInRow = []
xValues = []
rowValue = 2000000
for line in input:
    x1, y1, x2, y2 = [int(x) for x in re.findall('-?\d+', line)]
    distance = abs(y2 - y1) + abs(x2 - x1)
    sensors.append((x1, y1, distance))
    if y2 == rowValue:
        beaconsInRow.append(x2)
    xValues.append(x2)
ranges = []
for s in sensors:
    x, y, distance = s
    r = range(x + (abs(rowValue - y) - distance), x - (abs(rowValue - y) - distance) + 1)
    ranges.append(r)

result = 0
for i in range(min(xValues), max(xValues) + 1):
    outOfRange = True
    for r in ranges:
        if i in r:
            outOfRange = False
            break
    if not outOfRange and i not in beaconsInRow:
        result += 1
print(result)
