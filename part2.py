# i had to cut a piece of paper with the same shape as the input in order to make the visualization easier
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
def to3DCoords(coords):
    length = map.shape[0] / 4
    x = (coords[0] % length) + 0.5
    y = (coords[1] % length) + 0.5
    # sectionX and sectionY will be used to determine which face tank is currently on
    sectionX = coords[0] // length
    sectionY = coords[1] // length
    if (sectionX == 1) and (sectionY == 0): return (x, 0, y)
    if (sectionX == 2) and (sectionY == 0): return (length, x, y)
    if (sectionX == 1) and (sectionY == 1): return (x, y, length)
    if (sectionX == 1) and (sectionY == 2): return (x, length, length - y)
    if (sectionX == 0) and (sectionY == 2): return (0, x, length - y)
    if (sectionX == 0) and (sectionY == 3): return (y, x, 0)

    return None

def to2DCoords(coords):
    x = coords[0] - 0.5
    y = coords[1] - 0.5
    z = coords[2] - 0.5
    length = map.shape[0] / 4

    if x == -0.5: return (y, 3 * length - 1 - z)
    if x == length - 0.5: return (2 * length + y, z)
    if y == -0.5: return (length + x, z)
    if y == length - 0.5: return (length + x, 3 * length - 1 - z)
    if z == -0.5: return (y, 3 * length + x)
    if z == length - 0.5: return (length + x, length + y)
def moveForward(steps):
    global tank, facing
    nextTank = lambda: (tank[0] + facing[0], tank[1] - facing[1]) # Since "down" is increasing the y-value in an array, - facing[1] is used
    onEdge = lambda: (nextTank()[1] < 0 or nextTank()[1] >= map.shape[0]) or \
                     (nextTank()[0] < 0 or nextTank()[0] >= map.shape[1])
    length = map.shape[0] / 4
    for step in range(steps):
        tank2 = tank
        if onEdge() or map[nextTank()[1]][nextTank()[0]] == 0:
            tank3 = (tank[0], tank[1])  # This is some weird thing to deal with corner cases
            if facingValues[facing] == 0: tank3 = (tank[0], tank[1] // length * length + length // 2)
            if facingValues[facing] == 1: tank3 = (tank[0] // length * length + length // 2, tank[1])
            if facingValues[facing] == 2: tank3 = (tank[0], tank[1] // length * length + (length // 2))
            if facingValues[facing] == 3: tank3 = (tank[0] // length * length + length // 2, tank[1])
            cubeCoords = to3DCoords(tank)
            cubeCoords = list(cubeCoords)
            cubeCoords2 = to3DCoords(tank3)
            cubeCoords2 = list(cubeCoords2)
            for i in range(3):
                if cubeCoords2[i] == 0.0:
                    cubeCoords2[i] = 0.5
                    continue
                if cubeCoords2[i] == length:
                    cubeCoords2[i] = length - 0.5
                    continue
                if cubeCoords2[i] == 0.5: cubeCoords2[i] = 0.0
                if cubeCoords2[i] == length - 0.5: cubeCoords2[i] = length
            for i in range(3):
                if cubeCoords2[i] == 0.0:
                    cubeCoords[i] = 0.0
                    continue
                if (cubeCoords2[i] == length):
                    cubeCoords[i] = length
                    continue
                if cubeCoords2[i] == 0.5: cubeCoords[i] = 0.5
                if cubeCoords2[i] == length - 0.5: cubeCoords[i] = length - 0.5
            cubeCoords = tuple(cubeCoords)
            cubeCoords2 = tuple(cubeCoords2)
            tank = to2DCoords(cubeCoords)
            tank3 = to2DCoords(cubeCoords2)
            tank = (int(tank[0]), int(tank[1]))
            tank3 = (int(tank3[0]), int(tank3[1]))
            if map[tank[1]][tank[0]] == 1:
                tank = tank2
                break
            if tank3[0] % length == 0: facing = (1, 0)
            if tank3[0] % length == length - 1: facing = (-1, 0)
            if tank3[1] % length == 0: facing = (0, -1)
            if tank3[1] % length == length - 1: facing = (0, 1)
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