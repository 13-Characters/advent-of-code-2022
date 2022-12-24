# this is just like omega tank game 1989
import re
import numpy as np

input = open("input.txt").readlines()
tank = (input[0].index("."), 0) # (x, y)
facing = (1, 0)
for index, line in enumerate(reversed(input)):
    if re.match("\d+", line):
        instructions = line
        mapHeight = len(input) - index - 2
        break

instructions = instructions.replace("L", " L ")
instructions = instructions.replace("R", " R ")
instructions = instructions.split()
# 0=not on map, -1 = open, 1 = obstacle
map = np.zeros((mapHeight, max([len(line) for line in input[0:mapHeight]]) - 1), dtype=int)
for i in range(map.shape[0]):
    for j in range(map.shape[1]):
        if j < len(input[i]):
            if input[i][j] == ".":
                map[i][j] = -1
            if input[i][j] == "#":
                map[i][j] = 1

def turnLeft():
    global facing
    facing = (-facing[1], facing[0])
def turnRight():
    global facing
    facing = (facing[1], -facing[0])
def moveForward(steps):
    global tank, facing, hue
    nextTank = lambda: (tank[0] + facing[0], tank[1] - facing[1]) # Since "down" is increasing the y-value in an array, - facing[1] is used
    onEdge = lambda: (nextTank()[1] < 0 or nextTank()[1] >= map.shape[0]) or \
                     (nextTank()[0] < 0 or nextTank()[0] >= map.shape[1])
    for step in range(steps):
        if onEdge() or map[nextTank()[1]][nextTank()[0]] == 0:
            tank2 = tank
            prevTank = lambda: (tank[0] - facing[0], tank[1] + facing[1])
            tank = prevTank()
            while (not onEdge() and map[nextTank()[1]][nextTank()[0]] != 0):
                tank = prevTank()
            tank = nextTank()
            tank = nextTank()
            if map[tank[1]][tank[0]] == 1:
                tank = tank2
            continue
        if map[nextTank()[1]][nextTank()[0]] == -1:
            tank = nextTank()
            continue
        if map[nextTank()[1]][nextTank()[0]] == 1:
            break

for step in instructions:
    if re.match("\d+", step):
        moveForward(int(step))
    if step == "R":
        turnRight()
    if step == "L":
        turnLeft()
facingValues = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
result = 1000 * (tank[1] + 1) + 4 * (tank[0] + 1) + facingValues[facing]
print(result)
