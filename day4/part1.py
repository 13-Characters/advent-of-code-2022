input = open("input.txt")
count = 0
for line in input:
    range1, range2 = line.split(",")
    range1 = [int(x) for x in range1.split("-")]
    range2 = [int(x) for x in range2.split("-")]

    if (range2[1] - range2[0]) > (range1[1] - range1[0]):
        outer = range2
        inner = range1
    else:
        outer = range1
        inner = range2

    list = [outer[0], inner[0], inner[1], outer[1]]
    list2 = [range1[0], range1[1], range2[0], range2[1]]
    list2.sort()
    if list2 == list:
        count += 1
print(count)