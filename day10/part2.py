input = open("input.txt").readlines()
cycleNum = 1
X = 1
goodCycles = [20, 60, 100, 140, 180, 220]
result = 0
cmdInProgress = False
index = 0
counter = 0
addNext = 0
image = [''] * 240
while True == True:
    pixelPos = (cycleNum - 1) % 40
    if cycleNum <= 240 and abs(pixelPos - X) <= 1:
        image[cycleNum - 1] = '#'
    else:
        if cycleNum <= 240:
            image[cycleNum - 1] = '.'
    if cmdInProgress == False:
        line = input[index]
        if line.startswith("noop"):
            cmdInProgress = True
            counter = 1
            addNext = 0
        if line.startswith("addx"):
            cmdInProgress = True
            counter = 2
            addNext = int(line.split()[1])
    else:
        if counter != 0:
            counter -= 1
        if counter == 0:
            index = index + 1
            X += addNext
            if index >= len(input):
                break
            cmdInProgress = False
            cycleNum -= 1
    if cycleNum in goodCycles:
        result += (cycleNum * X)
        goodCycles.remove(cycleNum)
    cycleNum += 1


image = ''.join(image)
for i in range(6):
    print(image[0+40*i:40+40*i])
