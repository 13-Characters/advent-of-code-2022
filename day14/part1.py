import numpy as np
input = open("input.txt")

solidTiles = []
heights = []
for line in input: # Rock walls
    coords = line.split('->')
    coords = [(int(c.split(',')[0]), int(c.split(',')[1])) for c in coords]
    for i in range(len(coords) - 1):
        if coords[i][0] == coords[i + 1][0]: # If vertical
            t = [coords[i][1], coords[i + 1][1]]
            for j in range(min(t), max(t) + 1):
                solidTiles.append((coords[i][0], j))
        else: # If horizontal
            t = [coords[i][0], coords[i + 1][0]]
            for j in range(min(t), max(t) + 1):
                solidTiles.append((j, coords[i][1]))
                heights.append(coords[i][1])

abyss = max(heights)
sCoord = (500, 0)
result = 0
while sCoord[1] < abyss:
    if (sCoord[0], sCoord[1] + 1) in solidTiles:
        if (sCoord[0] - 1, sCoord[1] + 1) not in solidTiles: # Place down-left
            sCoord = (sCoord[0] - 1, sCoord[1] + 1)
        else:
            if (sCoord[0] + 1, sCoord[1] + 1) not in solidTiles: # Place down-right
                sCoord = (sCoord[0] + 1, sCoord[1] + 1)
            else: # Place directly above
                solidTiles.append((sCoord[0], sCoord[1]))
                sCoord = (500, 0)
                result += 1
    else:
        sCoord = (sCoord[0], sCoord[1] + 1)
print(result)
