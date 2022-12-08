import numpy as np
import re
input = open("input.txt")
input = input.readlines()
grid = np.zeros((len(input[0]) - 1, len(input)), int) # why -1 on the first parameter?? i don't even know
visibleTrees = [] # Need to convert this to set at the end since there will be duplicates

for row, line in enumerate(input):
    for column, char in enumerate(line[:-1]):
        grid[row][column] = int(char)

# This entire segment is too messy
# i = row #, j = column #
# Look from up/down:
for j in range(grid.shape[1]): # iterate every column
    up = [-1]
    down = [-1]
    for i in range(grid.shape[0]): # iterate every row
        currentUp = grid[i][j]
        currentDown = grid[grid.shape[0] - i - 1][j]
        if currentUp > max(up):
            visibleTrees.append((i, j))
        if currentUp >= max(up):
            up.append(currentUp)
        if currentDown > max(down):
            visibleTrees.append((grid.shape[0] - i - 1, j))
        if currentDown >= max(down):
            down.append(currentDown)

# Look from left/right
for i in range(grid.shape[0]): # iterate every column
    left = [-1]
    right = [-1]
    for j in range(grid.shape[1]): # iterate every row
        currentLeft = grid[i][j]
        currentRight = grid[i][grid.shape[1] - j - 1]
        if currentLeft > max(left):
            visibleTrees.append((i, j))
        if currentLeft >= max(left):
            left.append(currentLeft)
        if currentRight > max(right):
            visibleTrees.append((i, grid.shape[1] - j - 1))
        if currentRight >= max(right):
            right.append(currentRight)

visibleTrees = [*set(visibleTrees)]
print(len(visibleTrees))

grid = grid.astype(str)
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if (i, j) in visibleTrees:
            grid[i][j] = grid[i][j] + '*'

print(grid)