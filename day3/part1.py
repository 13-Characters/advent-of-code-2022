input = open("input.txt")

totalPriority = 0
for line in input:
    bothSacks = ''
    for char in line[:len(line) // 2]:
        if char in line[len(line) // 2:]:
            bothSacks = char
            break
    # since the ASCII values have the alphabet in order we can take advantage of this by not having to
    # make a list for the priorities
    if ord(bothSacks) > 96:
        priority = ord(char) - 96
    else:
        priority = ord(char) - 38
    totalPriority += priority

print(totalPriority)