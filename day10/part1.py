import numpy as np
import re
input = open("input.txt").readlines()
cycleNum = 1
X = 1
goodCycles = [20, 60, 100, 140, 180, 220]
result = 0
cmdInProgress = False
index = 0
counter = 0
addNext = 0
while True == True:
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
        print(cycleNum * X)
    cycleNum += 1

print(result)