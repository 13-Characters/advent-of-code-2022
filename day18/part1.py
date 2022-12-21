input = open("input.txt")
def isAdjacent(coord1, coord2):
    diff = [abs(coord1[i] - coord2[i]) for i in range(len(coord1))]
    if diff.count(0) == len(coord1) - 1 and diff.count(1) == 1:
        return True
    return False
coordList = []
for line in input:
    coordList.append(eval(f"({line})"))

area = 6 * len(coordList)
for c1 in coordList:
    for c2 in coordList:
        if c1 == c2: continue
        if isAdjacent(c1, c2): area -= 1

print(area)