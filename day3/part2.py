input = open("input.txt")

totalPriority = 0
inputList = []
# If I spent less time panicking about how to make a file a list I think I would've finished this part faster
for line in input:
    inputList.append(line)
i = 0
while (i < len(inputList)):
    common = ''
    for char in inputList[i]:
        if char in inputList[i + 1]:
            if char in inputList[i + 2]:
                common = char
                break
    if ord(common) > 96:
        priority = ord(char) - 96
    else:
        priority = ord(char) - 38
    totalPriority += priority
    i += 3

print(totalPriority)