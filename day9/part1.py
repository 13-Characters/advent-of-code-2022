import numpy as np
input = open("input.txt")
headPos = (0, 0)
tailPos = (0, 0)
tailPosL = []

for line in input:
    direction, num = line.split()
    num = int(num)
    for i in range(num):
        if direction == 'U':
            headPos = (headPos[0], headPos[1] + 1)
        if direction == 'R':
            headPos = (headPos[0] + 1, headPos[1])
        if direction == 'D':
            headPos = (headPos[0], headPos[1] - 1)
        if direction == 'L':
            headPos = (headPos[0] - 1, headPos[1])
        if abs(tailPos[1] - headPos[1]) > 1 or abs(tailPos[0] - headPos[0]) > 1:
            tailPos = (tailPos[0] - np.sign(tailPos[0] - headPos[0]), tailPos[1] - np.sign(tailPos[1] - headPos[1]))
        tailPosL.append(tailPos)

tailPosL = [*set(tailPosL)]
part_1_result = len(tailPosL)
print(part_1_result)
