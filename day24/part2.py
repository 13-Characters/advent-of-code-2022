import re
import numpy as np
input = open("input.txt").readlines()

width = len(re.sub("[#\n]", "", input[1]))
height = []
for line in input:
    if re.search("[\^v<>]", line):
        height.append(line)
height = len(height)
up, left, down, right = np.zeros((height, width)), np.zeros((height, width)), np.zeros((height, width)), np.zeros((height, width))
valley = lambda: np.sum(np.array([up, down, left, right]), axis=0) # I am starting to overuse lambda functions

for row in range(height):
    for column in range(width):
        if input[row + 1][column + 1] == "^":
            up[row][column] = 1
        if input[row + 1][column + 1] == "<":
            left[row][column] = 1
        if input[row + 1][column + 1] == "v":
            down[row][column] = 1
        if input[row + 1][column + 1] == ">":
            right[row][column] = 1
start = (0, input[0].index("."))
end = (len(input) - 1, input[-1].index("."))
pathsList = [[(start, (-1, -1))]] # every element will list a coordinate as well as a reference to the previous position
minutes = 0
stage = 0 # Keeps track if we are going forward or backward
while True:
    current = []
    for index, element in enumerate(pathsList[-1]):
        coord = element[0]
        nextCoords = [((coord[0] - 1, coord[1]), coord), ((coord[0] + 1, coord[1]), coord),
                      ((coord[0], coord[1] - 1), coord), ((coord[0], coord[1] + 1), coord),
                      (coord, coord)]
        isPassable = lambda coord: (coord[0] - 1 >= 0 and coord[0] - 1 < height and coord[1] - 1 >= 0 and coord[1] - 1 < width \
                                   and valley()[coord[0] - 1][coord[1] - 1] == 0) or (coord == start or coord == end)
        for n in nextCoords:
            if isPassable(n[0]):
                current.append(n)
    minutes += 1
    current = [*set(current)]
    pathsList.append(current)
    if end in [c[0] for c in current] and (stage == 0 or stage == 2):
        if stage == 2:
            minutes -= 1
            break
        else:
            pathsList = [[(end, (end[0] + 1, end[0] + 1))]]
            stage = 1
    else:
        if start in [c[0] for c in current] and (stage == 1):
            pathsList = [[(start, (-1, -1))]]
            stage = 2
    # Update the blizzard positions
    down = np.roll(down, 1, axis=0)
    up = np.roll(up, -1, axis=0)
    right = np.roll(right, 1, axis=1)
    left = np.roll(left, -1, axis=1)

print(minutes)