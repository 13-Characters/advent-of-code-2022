import numpy as np
input = open("input.txt")
tailsPos = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
tail9PosL = []

for line in input:
    direction, num = line.split()
    num = int(num)
    for i in range(num):
        if direction == 'U':
            tailsPos[0] = (tailsPos[0][0], tailsPos[0][1] + 1)
        if direction == 'R':
            tailsPos[0] = (tailsPos[0][0] + 1, tailsPos[0][1])
        if direction == 'D':
            tailsPos[0] = (tailsPos[0][0], tailsPos[0][1] - 1)
        if direction == 'L':
            tailsPos[0] = (tailsPos[0][0] - 1, tailsPos[0][1])
        for n in range(len(tailsPos)):
            if n > 0 and (abs(tailsPos[n][1] - tailsPos[n - 1][1]) > 1 or abs(tailsPos[n][0] - tailsPos[n - 1][0]) > 1):
                tailsPos[n] = (tailsPos[n][0] - np.sign(tailsPos[n][0] - tailsPos[n - 1][0]),
                           tailsPos[n][1] - np.sign(tailsPos[n][1] - tailsPos[n - 1][1]))
        tail9PosL.append(tailsPos[9])

tail9PosL = [*set(tail9PosL)]
part_2_result = len(tail9PosL)
print(part_2_result)
