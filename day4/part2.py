input = open("input.txt")
count = 0
for line in input:
    range1, range2 = line.split(",")
    range1 = [int(x) for x in range1.split("-")]
    range2 = [int(x) for x in range2.split("-")]

    if (range2[1]) > (range1[1]):
        upper = range2
        lower = range1
    else:
        upper = range1
        lower = range2

    list = [lower[0], lower[1], upper[0], upper[1]]
    list2 = [range1[0], range1[1], range2[0], range2[1]]
    list2.sort()
    if list2 != list:
        count += 1
    else:
        if list[1] == list[2]:
            count += 1
print(count)