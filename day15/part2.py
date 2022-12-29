# Isn't it weird that this runs much faster than part 1
import re
input = open("input.txt")

sensors = []
beaconsInRow = []
xValues = []
rowValue = 0
for line in input:
    x1, y1, x2, y2 = [int(x) for x in re.findall('-?\d+', line)]
    distance = abs(y2 - y1) + abs(x2 - x1)
    sensors.append((x1, y1, distance))
    if y2 == rowValue:
        beaconsInRow.append(x2)
    xValues.append(x2)
ranges = []
endpoints = []
for s in sensors:
    x, y, distance = s
    e = [x + (y - distance), x - (y - distance), x + (y + distance), x - (y + distance)]
    endpoints += e

xints = []
for e in endpoints:
    if e + 2 in endpoints:
        xints.append(e + 1)

result = 0
for ind, i in enumerate(xints):
    for j in xints[ind + 1:]:
        if i == j:
            continue
        else:
            x = (i + j) // 2
            y = x - i
            ranges = [range(s[0] + (abs(y - s[1]) - s[2]), s[0] - (abs(y - s[1]) - s[2]) + 1) for s in sensors]
            if all([x not in r for r in ranges]):
                result = 4000000 * x + y
                print(result)
                break
            y = -y
            ranges = [range(s[0] + (abs(y - s[1]) - s[2]), s[0] - (abs(y - s[1]) - s[2]) + 1) for s in sensors]
            if all([x not in r for r in ranges]):
                result = 4000000 * x + y
                print(result)
                break